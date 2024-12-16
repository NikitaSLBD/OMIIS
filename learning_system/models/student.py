from typing import TYPE_CHECKING
from models.user import User

if TYPE_CHECKING:
    from models.course import Course
    from models.progress import Progress

class Student(User):

    def __init__(self, id: int, name: str, email: str, password: str):

        super().__init__(id, name, email, password)
        self.__registered_courses: list[Course] = []
        self.__progress: dict[Course: Progress] = dict()

    def get_registered_courses(self) -> list[Course]: return self.__registered_courses
    def get_progress(self) -> dict[Course: Progress]: return self.__progress

    def update_progress(self, course: Course, new_progress: Progress): self.__progress[course] = new_progress
    def register_for_course(self, course: Course): self.__registered_courses.append(course)