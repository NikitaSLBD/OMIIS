from typing import TYPE_CHECKING
from models.interfaces.i_student_repo import I_student_repo

if TYPE_CHECKING:
    from models.student import Student

class Student_service(I_student_repo):

    __students = []

    @classmethod
    def save(cls, student: Student): cls.__students.append(student)

    @classmethod
    def find_by_id(cls, id: int) -> Student | None: 
        for student in cls.__students:
            if id == student.get_id(): return student
        
    @classmethod
    def find_all(cls) -> list[Student]: return cls.__students 
