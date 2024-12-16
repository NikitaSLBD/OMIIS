from typing import TYPE_CHECKING
from models.user import User

if TYPE_CHECKING:
    from datetime import date
    from models.course import Course

class Teacher(User):

    def __init__(self, id: int, name: str, email: str, password: str):

        super().__init__(id, name, email, password)
        self.__courses: list[Course] = [] 

    def get_courses(self) -> list[Course]: return self.__courses

    def create_course(name: str, start: date, end: date) -> Course: pass 
    def update_course(course: Course): pass
    def delete_course(course_id: int): pass