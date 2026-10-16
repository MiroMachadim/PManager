from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional
from db_instance import db

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

    @abstractmethod
    def handle(self,request: db.Model,dados: dict) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request,dados)
        return None
