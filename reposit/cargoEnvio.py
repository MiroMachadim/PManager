from typing import Optional

from db_instance import db
from model.Cargo import  Cargo
from reposit.handler import AbstractHandler


class NomeHandler(AbstractHandler):
    def handle(self,request,dados: dict) -> Optional[str]:
        nome = dados.get('nome')
        if nome:
            request.c.nome = nome
        return super().handle(request,dados)

class PosicaoHandler(AbstractHandler):
    def handle(self,request,dados: dict) -> Optional[str]:
        pos = dados.get('posicao')
        if pos:
            request.c.posicao = pos
        return super().handle(request,dados)


def enviar_cargo(nome, pos):
    cargo = Cargo()
    cargo.c.nome = nome
    cargo.c.posicao = pos
    db.session.add(cargo)

    return db.session.commit()

def upd_cargo(id,nome,posicao):
    cargo = db.session.get(Cargo,id)
    dados = {'nome':nome,'posicao':posicao}
    if cargo:
        nomehandle = NomeHandler()
        posihandle = PosicaoHandler()
        cadeia = nomehandle.set_next(posihandle)
        cadeia.handle(cargo,dados)
        return db.session.commit()
    else:
        raise Exception("cargo nao encontrado")