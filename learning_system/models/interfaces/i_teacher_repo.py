from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.teacher import Teacher

class I_teacher_repo:

    def save(teacher: Teacher): pass
    def find_by_id(id: int) -> Teacher | None: pass
    def find_all() -> list[Teacher]: pass