from typing import TYPE_CHECKING
from uuid import uuid1

if TYPE_CHECKING:
    from models.assignment import Assignment

class Module:

    def __init__(self, title: str, content: str, id: int=0):

        self.__id: int = uuid1.int() if not id else id
        self.__title: str = title
        self.__content: str = content
        self.__assignments = []

    def get_id(self) -> int: return self.__id
    def get_title(self) -> str: return self.__title
    def get_assignments(self) -> list[Assignment]: return self.__assignments
    def get_content(self) -> str: return self.__content

    def set_title(self, title: str): 
        self.__title = title
    
    def add_assignment(self, assignment: Assignment): self.__assignments.append(assignment)