from typing import TYPE_CHECKING
from models.interfaces.i_teacher_repo import I_teacher_repo

if TYPE_CHECKING:
    from models.teacher import Teacher
 
class Teacher_service(I_teacher_repo):

    __teachers = []

    @classmethod
    def save(cls, student: Teacher): cls.__teachers.append(student)

    @classmethod
    def find_by_id(cls, id: int) -> Teacher | None: 
        for teacher in cls.__teachers:
            if id == teacher.get_id(): return teacher
        
    @classmethod
    def find_all(cls) -> list[Teacher]: return cls.__teachers 
