from datetime import datetime
from db_instance import db
from model.Ocorrencia import Bo
from typing import Optional
from handler import AbstractHandler


class AtualizarMetaHandler(AbstractHandler):
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        request.c.updated_by = dados.get("cpf")
        request.c.updated_at = datetime.now()
        return super().handle(request,dados)

class AtualizarEstadoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        veri = dados.get("estado")
        if veri:
            pass
        else:
            request.c.estado = veri
        return super().handle(request,dados)

class AtualizarLocalidadeHandler(AbstractHandler):
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        local = dados.get("localidade")
        if local:
            pass
        else:
            request.c.localidade = local
        return super().handle(request,dados)

class AtualizarConteudoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        conteudo = dados.get("conteudo")
        if conteudo:
            pass
        else:
            request.c.conteudo = conteudo
        return super().handle(request,dados)

class AtualizarTipoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        tipo = dados.get("tipo")
        if tipo:
            pass
        else:
            request.c.tipo_id = tipo
        return super().handle(request,dados)


def enviar_bo(cpf,estado,tipo,localidade,conteudo):
    bo = Bo()
    bo.c.created_at = datetime.now()
    bo.c.created_by = cpf
    bo.c.estado = estado
    bo.c.tipo_id = tipo
    bo.c.localidade = localidade
    bo.c.estado = estado
    bo.c.conteudo = conteudo

    db.session.add(bo)

    return db.session.commit()

def upd_bo(id,usuario,tipo,localidade,conteudo,estado):
    bo = db.session.get(Bo,id)
    dados = {"cpf":usuario,"tipo":tipo,"localidade":localidade,"estado":estado,"conteudo":conteudo}
    if bo:
        metahandle = AtualizarConteudoHandler()
        estadohandle = AtualizarEstadoHandler()
        conteudohandle = AtualizarConteudoHandler()
        localidadehandle = AtualizarLocalidadeHandler()
        tipohandle = AtualizarTipoHandler()
        ordem = metahandle.set_next(estadohandle).set_next(conteudohandle).set_next(localidadehandle).set_next(tipohandle)
        ordem.handle(bo,dados)
        db.session.commit()
    else:
        raise Exception("bo nao encontrado")
