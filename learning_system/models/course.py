from typing import TYPE_CHECKING
from uuid import uuid1

if TYPE_CHECKING:
    from datetime import date
    from models.module import Module

class Course:

    def __init__(self, name: str, start: date, end: date, id: int=0):

        self.__id: int = uuid1.int() if not id else id
        self.__name: str = name
        self.__description
        self.__start_date: date = start
        self.__end_date: date = end
        self.__modules = []

    def get_id(self) -> int: return self.__id
    def get_name(self) -> str: return self.__name
    def get_start(self) -> date: return self.__start_date
    def get_end(self) -> date: return self.__end_date
    def get_modules(self) -> list[Module]: return self.__modules

    def set_name(self, name: str): self.__name = name

    def add_module(self, module: Module): self.__modules.append(module)