from design_patterns.factory_method.base_employee_factory import BaseEmployeeFactory
from design_patterns.factory_method.contract_employee_manager import ContractEmployeeManager


class ContractEmployeeFactory(BaseEmployeeFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        manager = ContractEmployeeManager()
        self.emp['insurance'] = manager.get_medical_allowance()
        return manager

