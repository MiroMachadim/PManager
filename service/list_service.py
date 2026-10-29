from select import select
import reposit.conexao_banco as cb
import model
import reposit.busca_banco as busca


def pedir_ocorrencias():
    return cb.listar(model.Ocorrencia.Bo())

def pedir_pessoa(cpf):
    return cb.selecionar_por_cpf(model.Pessoa.Pessoa(),cpf)

def listar_bo_ficha(cpf):
    bo = model.Ocorrencia.Bo()
    stmt = (bo.c.cpf_vitima == cpf)
    return busca.buscar(bo,stmt)

def listar_fichas():
    pessoa = model.Pessoa.Pessoa()
    bo = model.Ocorrencia.Bo()
    ficha = model.Ficha.Ficha()
    stmt = select(
            ficha.c.id.label("id"),
            pessoa.c.nome.label("nome"),
            pessoa.c.cpf.label("cpf"),
            bo.c.id.label("bo_id"),
            bo.c.conteudo.label("data_bo")
          ).select_from(ficha).join(pessoa,ficha.c.cpf == pessoa.c.cpf).join(bo, ficha.c.bo_id == bo.c.id)
    return busca.join_ficha(stmt)