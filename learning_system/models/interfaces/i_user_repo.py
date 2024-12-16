from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from models.user import User

class I_user_repo:

    def save(student: User): pass
    def find_by_id(id: int) -> User | None: pass