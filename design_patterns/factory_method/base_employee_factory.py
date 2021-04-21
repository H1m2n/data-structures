# This class will provide permanent or contract employee object on basis of there
# employee type
from abc import abstractmethod

from design_patterns.simple_factory.contract_employee_manager import ContractEmployeeManager
from design_patterns.simple_factory.permanent_employee_manager import PermanentEmployeeManager


# This is the base class of factories and should be abstract
class BaseEmployeeFactory:
    def __init__(self):
        self.emp = {}

    # This function will be responsible to create manager on basis of the condition
    @abstractmethod
    def create(self):
        pass

    def apply_salary(self):
        manager = self.create()
        self.emp['bonus'] = manager.get_bonus()
        self.emp['payscale'] = manager.get_payscale()
