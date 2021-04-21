# This needs to be abstract class that will return employee manager with extended properties
from design_patterns.factory_method.contract_employee_factory import ContractEmployeeFactory
from design_patterns.factory_method.employee_manager import EmployeeManager
from design_patterns.factory_method.permanent_employee_factory import PermanentEmployeeFactory


class EmployeeManagerFactory:
    def __init__(self):
        pass

    def create_factory(self, emp_type):
        if emp_type == 1:
            return PermanentEmployeeFactory()
        else:
            return ContractEmployeeFactory()
