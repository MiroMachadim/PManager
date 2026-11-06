import os
from flask import abort, flash
import reposit.conexao_banco as cb
from datetime import datetime, timezone
from werkzeug.utils import secure_filename
import reposit.busca_banco as be
from model.Pessoa import Pessoa
from model.Falta import Falta
from service.user_service import adquirir_cpf
from model.Tipo import Tipo
from model.Estado import Estado
from model.Cargo import Cargo
from model.Ocorrencia import Bo
from model.Ficha import Ficha


def enviar_pessoa(dados:dict):

    cpf = dados.get("cpf")
    cpf_bruto = adquirir_cpf(cpf)

    dados.update({"cpf": cpf_bruto})
    sexo = dados.get("sexo")
    if sexo == "Masculino":
        dados.update({"sexo": "M"})
    elif sexo == "Feminino":
        dados.update({"sexo": "F"})
    elif sexo == "Outro":
        dados.update({"sexo": "O"})
    data_nascimento = dados.get("data_nascimento")
    if data_nascimento:
        dados.update({"data_nascimento": converter_data(data_nascimento)})
    else:
        return False

    existe = cb.selecionar_por_cpf(Pessoa, cpf_bruto)
    if not existe:
        print(dados.get("cpf"))
        return cb.inserir_dados(Pessoa, dados, 4)
    else:
        flash("pessoa já existente")
        return False

def converter_data(data: str):
    try:
        return datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Data inválida: '{data}'. Formato esperado: AAAA-MM-DD")


def cadastrar_ocorrencia(dados: dict):
    dados["created_at"] = setar_data()
    cpf = dados.get("cpf")
    cpf_bruto = adquirir_cpf(cpf)
    dados.update({"cpf_vitima":cpf_bruto})
    dados.pop("cpf")
    nome = dados.get("tipo")
    tipo_id = be.id_por_nome(Tipo, nome)
    dados.update({"tipo_id": tipo_id})
    dados.pop("tipo")
    estado = dados.get("estado_id")
    estado_id = be.id_por_nome(Estado, estado)
    dados.update({"estado_id": estado_id})

    if not cb.selecionar_por_cpf(Pessoa,cpf_bruto):
        flash("vítima não presente no banco")
        return False
    print(dados)
    return cb.inserir_dados(Bo, dados, 7)

def inserir_suspeito(cpf, bo_id):
    if cpf:
        cpf = adquirir_cpf(cpf)
    pessoa = cb.selecionar_por_cpf(Pessoa,cpf)
    if pessoa:
        dados = {
            "cpf": cpf,
            "bo_id": bo_id
        }
        return cb.inserir_dados(Ficha,dados,2)


def enviar_falta(dados: dict):
    from main import ALLOWED_EXTENSIONS
    from main import app

    upload_folder = app.config["UPLOAD_FOLDER"]
    os.makedirs(upload_folder, exist_ok=True)

    arquivo = dados.get("arquivo_falta")

    data_inicio = dados.get("data_inicio")
    data_correta = converter_data(data_inicio)
    data_final = dados.get("data_fim")
    data_fim_correta = converter_data(data_final)

    dados.update({"data_inicio":data_correta})
    dados.update({"data_fim":data_fim_correta})

    dados.update({"created_at": setar_data()})


    if arquivo is None:
        abort(400, "Arquivo de falta não enviado")

    filename = secure_filename(arquivo.filename)

    if not filename or "." not in filename:
        abort(400, "Nome de arquivo inválido")

    file_ext = filename.rsplit(".", 1)[1].lower()
    if file_ext not in ALLOWED_EXTENSIONS:
        abort(400, "Extensão não permitida")

    arquivo.save(os.path.join(upload_folder,filename))

    dados.pop("arquivo_falta")
    dados["justificativa"] = filename
    print(dados)
    return cb.inserir_dados(Falta, dados, 5)


def setar_data():
    return datetime.now(timezone.utc)


def atualizar_ocorrencia(dados: dict):
    id_ocorrencia = dados.get("id")
    if id_ocorrencia is None:
        abort(400, "id é obrigatório para atualização")

    instance = cb.instanciar(Bo, id_ocorrencia)
    if instance is None:
        abort(404, "Ocorrência não encontrada")


    dados["updated_at"] = setar_data()
    estado = dados.get("estado_id")
    if estado:
        estado_id = be.id_por_nome(Estado, estado)
        dados.update({"estado_id": estado_id})
    cpf = dados.get("cpf_vitima")
    if cpf:
        cpf_bruto = adquirir_cpf(cpf)
        dados.update({"cpf_vitima": cpf_bruto})
        if not cb.selecionar_por_cpf(Pessoa, cpf_bruto):
            flash("Pessoa inexistente")
            return False
    tipo = dados.get("tipo_id")
    if tipo:
        tipo_id = be.id_por_nome(Tipo, tipo)
        dados.update({"tipo_id": tipo_id})
    campos_validos = {
        k: v for k, v in dados.items()
        if v is not None and k != "id"
    }
    dados.clear()
    dados.update(campos_validos)

    return cb.inserir_dados(instance, dados, len(campos_validos))

def atualizar_parametros(dados:dict, total: int):
    categoria = dados.get("categoria")
    if categoria == "tipo_crime":
        tabela = Tipo
    elif categoria == "status_ocorrencia":
        tabela = Estado
    elif categoria == "cargo":
        tabela = Cargo
    else:
        flash("escolha uma opção válida")
        abort(400)
    nome_item = dados.get("nome")
    if not nome_item:
        flash("informe o nome do item")
        return False
    existe = be.buscar(tabela, tabela.nome == nome_item)
    if existe:
        flash("item já existe")
        return False
    else:
        dados.pop("categoria")
        print(dados.get("nome"))
        return cb.inserir_dados(tabela, dados, total)

