from typing import TYPE_CHECKING
from models.interfaces.i_course_repo import I_course_repo

if TYPE_CHECKING:
    from models.course import Course


class Course_service(I_course_repo):

    __courses = []

    @classmethod
    def save(cls, course: Course): cls.__courses.append(course)

    @classmethod
    def find_by_id(cls, id: int) -> Course | None: 
        for course in cls.__courses:
            if id == course.get_id(): return course
        
    @classmethod
    def find_all(cls) -> list[Course]: return cls.__courses 