import os
from os import abort
from model.Ocorrencia import Bo
import reposit.conexao_banco as cb
import reposit.insercao_banco as ib
from datetime import datetime, timezone
from werkzeug.utils import secure_filename


def cadastrar_ocorrencia(dados: dict):
    created_at = setar_data()
    dados.update({"created_at": created_at})
    enviado = cb.inserir_dados(Bo,dados,7)
    return enviado


def enviar_falta(dados: dict):
    from main import app
    arquivo = dados.get("arquivo_falta")
    created_at = setar_data()
    dados.update({"created_at": created_at})
    filename = secure_filename(arquivo)
    if filename:
        file_ext = filename.rsplit('.', 1)[1].lower()
        if file_ext not in app.config['ALLOWED_EXTENSIONS']:
            abort(400)
        arquivo.save(os.path.join,app.config["UPLOAD_FOLDER"], filename)
        dados.update({"arquivo_falta": filename})
    return cb.inserir_dados(Bo,dados,5)



def setar_data():
    return datetime.now(timezone.utc)

def atualizar_ocorrencia(dados:dict):
    id = dados.get("id")
    instance = cb.instanciar(Bo,id)
    updated_at = setar_data()
    dados.update({"updated_at": updated_at})
    chaves = dados.keys()
    quantia_upd = 0
    for chave in chaves:
        if chaves.get(chave) is None or chave == "id":
            dados.pop(chave)
        else:
            quantia_upd += 1
    cb.inserir_dados(instance,dados,quantia_upd)
    return ib
