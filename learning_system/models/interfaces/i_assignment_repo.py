from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.assignment import Assignment


class I_assignment_repo:

    def save(assignment: Assignment): pass
    def find_by_id(id: int) -> Assignment | None: pass