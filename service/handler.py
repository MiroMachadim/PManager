from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from db_instance import db

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def set_feito(self):
        pass

    @abstractmethod
    def handle(self,request,dados:dict,total=0) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Handler = None
    _feito: int = 0

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def set_feito(self):
        AbstractHandler._feito += 1

    @abstractmethod
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        if self._next_handler and self._feito != total:
            return self._next_handler.handle(request,dados,total)
        AbstractHandler._feito = 0
        return None

def verificar_nome(nome):
    for letra in nome:
        if letra == ' ' and letra.isalpha():
            continue
        else:
            raise Exception()
    return nome

class CpfHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        cpf = dados.get('cpf')
        if cpf:
            request.c.cpf= cpf
            super().set_feito()
        return super().handle(request,dados,total)

class NomeHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        nome = dados.get('nome')
        if nome:
            verificar_nome(nome)
            request.c.nome = nome
            super().set_feito()
        return super().handle(request,dados,total)

class SexoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        sexo = dados.get('sexo')
        if sexo:
            request.c.sexo = sexo
            super().set_feito()
        return super().handle(request,dados,total)

class AdminHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        admin = dados.get('admin')
        if admin:
            request.c.admin = admin
            super().set_feito()
        return super().handle(request,dados,total)

class IdadeHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        idade = dados.get('idade')
        if idade:
            request.c.idade = idade
            super().set_feito()
        return super().handle(request,dados,total)

class CargoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        cargo = dados.get('cargo')
        if cargo:
            request.c.cargo = cargo
            super().set_feito()
        return super().handle(request,dados,total)


class PosicaoHandler(AbstractHandler):
    def handle(self, request: db.Model, dados: dict, total=0) -> Optional[str]:
        posicao = dados.get('posicao')
        if posicao:
            request.c.posicao = posicao
            super().set_feito()
        return super().handle(request, dados, total)

class SenhaHandler(AbstractHandler):
    def handle(self, request: db.Model, dados: dict, total=0) -> Optional[str]:
        senha = dados.get('senha')
        if senha:
            request.c.senha = senha
            super().set_feito()
        return super().handle(request, dados, total)


class CargoIdHandler(AbstractHandler):
    def handle(self, request: db.Model, dados: dict, total=0) -> Optional[str]:
        cargo_id = dados.get('cargo_id')
        if cargo_id:
            request.c.cargo_id= cargo_id
            super().set_feito()
        return super().handle(request, dados, total)

class CepHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        cep = dados.get('cep')
        if cep:
            request.c.cep = cep
            super().set_feito()
        return super().handle(request, dados, total)

class AreaIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        area_id = dados.get('area_id')
        if area_id:
            request.c.area_id = area_id
            super().set_feito()
        return super().handle(request, dados, total)

class ZonaIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        zona_id = dados.get('zona_id')
        if zona_id:
            request.c.zona_id = zona_id
            super().set_feito()
        return super().handle(request, dados, total)

class PolicialIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        policial_id = dados.get('policial_id')
        if policial_id:
            request.c.policial_id = policial_id
            super().set_feito()
        return super().handle(request, dados, total)

class SetorIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        setor_id = dados.get('setor_id')
        if setor_id:
            request.c.setor_id = setor_id
            super().set_feito()
        return super().handle(request, dados, total)

class CreatedAtHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        created_at = dados.get('created_at')
        if created_at:
            request.c.created_at = created_at
            super().set_feito()
        return super().handle(request, dados, total)


class DataFimHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        data_fim = dados.get('data_fim')
        if data_fim:
            request.c.data_fim = data_fim
            super().set_feito()
        return super().handle(request, dados, total)

class JustificativaHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        justificativa = dados.get('justificativa')
        if justificativa:
            request.c.justificativa = justificativa
            super().set_feito()
        return super().handle(request, dados, total)

class TipoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        tipo = dados.get('tipo')
        if tipo:
            request.c.tipo = tipo
            super().set_feito()
        return super().handle(request, dados, total)

class EstadoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        estado = dados.get('estado')
        if estado:
            request.c.estado = estado
            super().set_feito()
        return super().handle(request, dados, total)

class UpdatedAtHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        updated_at = dados.get('updated_at')
        if updated_at:
            request.c.updated_at = updated_at
            super().set_feito()
        return super().handle(request, dados, total)

class CreatedByHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        created_by = dados.get('created_by')
        if created_by:
            request.c.updated_at = created_by
            super().set_feito()
        return super().handle(request, dados, total)

class UpdatedByHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        updated_by = dados.get('updated_by')
        if updated_by:
            request.c.updated_by = updated_by
            super().set_feito()
        return super().handle(request, dados, total)

class TipoIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        tipo_id = dados.get('tipo_id')
        if tipo_id:
            request.c.tipo_id= tipo_id
            super().set_feito()
        return super().handle(request, dados, total)

class ConteudoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        conteudo = dados.get('conteudo')
        if conteudo:
            request.c.conteudo = conteudo
            super().set_feito()
        return super().handle(request, dados, total)

class EstadoIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        estado_id = dados.get('estado_id')
        if estado_id:
            request.c.estado_id = estado_id
            super().set_feito()
        return super().handle(request, dados, total)

class BoIdHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        bo_id = dados.get('bo_id')
        if bo_id:
            request.c.bo_id = bo_id
            super().set_feito()
        return super().handle(request, dados, total)

class CulpadoHandler(AbstractHandler):
    def handle(self,request: db.Model,dados:dict,total=0) -> Optional[str]:
        culpado = dados.get('culpado')
        if culpado:
            request.c.culpado = culpado
            super().set_feito()
        return super().handle(request,dados,total)

