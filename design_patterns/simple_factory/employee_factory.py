# This class will provide permanent or contract employee object on basis of there
# employee type
from design_patterns.simple_factory.contract_employee_manager import ContractEmployeeManager
from design_patterns.simple_factory.permanent_employee_manager import PermanentEmployeeManager


class EmployeeFactory:
    def __init__(self):
        pass

    def get_employee_manager(self, employee_type):
        if employee_type == 1:
            return PermanentEmployeeManager()
        else:
            return ContractEmployeeManager()
