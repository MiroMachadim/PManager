from __future__ import annotations
from datetime import datetime
from db_instance import db
from model.Ocorrencia import Bo
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self,request,dados: dict) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request,dados)
        return None

class AtualizarMetaHandler(AbstractHandler):
    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        request.updated_by = dados.get("cpf")
        request.updated_at = datetime.now()
        return super().handle(request,dados)

class AtualizarEstadoHandler(AbstractHandler):
    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        veri = dados.get("estado")
        if veri:
            pass
        else:
            request.estado = veri
        return super().handle(request,dados)

class AtualizarLocalidadeHandler(AbstractHandler):
    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        local = dados.get("localidade")
        if local:
            pass
        else:
            request.localidade = local
        return super().handle(request,dados)

class AtualizarConteudoHandler(AbstractHandler):
    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        conteudo = dados.get("conteudo")
        if conteudo:
            pass
        else:
            request.conteudo = conteudo
        return super().handle(request,dados)

class AtualizarTipoHandler(AbstractHandler):
    def handle(self,request: Bo,dados: dict) -> Optional[str]:
        tipo = dados.get("tipo")
        if tipo:
            pass
        else:
            request.tipo_bo = tipo
        return super().handle(request,dados)


def enviarBo(cpf,estado,tipo,localidade,conteudo):
    bo = Bo()
    bo.created_at = datetime.now()
    bo.created_by = cpf
    bo.estado = estado
    bo.tipo_bo = tipo
    bo.localidade = localidade
    bo.estado = estado
    bo.conteudo = conteudo

    db.session.add(bo)

    return db.session.commit()

def updBo(id,usuario,tipo,localidade,conteudo,estado):
    bo = db.session.get(Bo,id)
    dadosUpd = {"cpf":usuario,"tipo":tipo,"localidade":localidade,"estado":estado,"conteudo":conteudo}
    if bo:
        AtualizarMetaHandler().handle(bo,dadosUpd)
    else:
        raise Exception("bo nao encontrado")
