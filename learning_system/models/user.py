class User:

    def __init__(self, id: int, name: str, email: str, password: str):

        self.__id: int = id
        self.__name: str = name
        self.__email: str = email
        self.__password: str = password

    def get_id(self) -> int: return self.__id
    def get_name(self) -> str: return self.__name
    def get_email(self) -> str: return self.__email
    def get_password(self) -> str: return self.__password

    def set_email(self, email: str): self.__email = email
    def set_password(self, password: str): self.__password = password





 

