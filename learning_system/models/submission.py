from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import date


class Submission:

    def __init__(self, content: str, date_: date, grade: int):

        self.__content: str = content
        self.__date: date = date_
        self.__grade: int = grade

    def get_content(self) -> str: return self.__content
    def get_date(self) -> date: return self.__date
    def get_grade(self) -> int: return self.__grade
    
    def set_grade(self, grade: int): self.__grade = grade