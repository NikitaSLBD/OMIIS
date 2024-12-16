from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.course import Course

class I_course_repo:

    def save(course: Course): pass
    def find_by_id(id: int) -> Course | None: pass
    def find_all() -> list[Course]: pass