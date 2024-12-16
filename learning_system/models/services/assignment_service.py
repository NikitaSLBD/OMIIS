from typing import TYPE_CHECKING
from models.interfaces.i_assignment_repo import I_assignment_repo

if TYPE_CHECKING:
    from models.assignment import Assignment


class Assignment_service(I_assignment_repo):

    __assignments = []

    @classmethod
    def save(cls, assignment: Assignment): cls.__assignments.append(assignment)

    @classmethod
    def find_by_id(cls, id: int) -> Assignment | None: 
        for assignment in cls.__assignments:
            if id == assignment.get_id(): return assignment 