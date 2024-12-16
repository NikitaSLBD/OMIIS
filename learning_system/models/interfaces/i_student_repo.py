from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.student import Student

class I_student_repo:

    def save(student: Student): pass
    def find_by_id(id: int) -> Student | None: pass
    def find_all() -> list[Student]: pass