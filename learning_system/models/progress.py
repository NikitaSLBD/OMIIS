from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from models.module import Module

class Progress:

    def __init__(self):

        self.__completed_modules = []
        self.__grades = dict()
    
    def get_completed_modules(self) -> list[Module]: return self.__completed_modules
    def get_grade(self, module: Module) -> int: return self.__grades[module]

    def modules_avg_grade(self, modules: list[Module]) -> float: 
        return sum([grade for module, grade in self.__grades.items() if module in modules]) / len(modules)

    def period_avg_grade(self, start: date, end: date) -> float: 

        modules = [module for module, _ in self.__grades.items() if module]
        return self.modules_avg_grade(modules)
