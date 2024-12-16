from typing import TYPE_CHECKING
from uuid import uuid1

if TYPE_CHECKING:
    from datetime import date
    from models.student import Student
    from models.submission import Submission

class Assignment:

    def __init__(self,  title: str, description: str, deadline: date, id: int=0):

        self.__id: int = uuid1.int() if not id else id
        self.__title: str = title
        self.__description: str = description
        self.__deadline: date = deadline
        self.__submitted_by = dict()

    def get_id(self) -> int: return self.__id
    def get_title(self) -> str: return self.__title
    def get_description(self) -> str: return self.__description
    def get_deadline(self) -> date: return self.__deadline

    def submit(self, student: Student, submission: Submission): self.__submitted_by: dict[Student: Submission] = {student: submission}
    def evaluate(self, student: Student, grade: int): self.__submitted_by[student].set_grade(grade)