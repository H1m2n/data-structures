from design_patterns.factory_method.base_employee_factory import BaseEmployeeFactory
from design_patterns.factory_method.permanent_employee_manager import PermanentEmployeeManager


class PermanentEmployeeFactory(BaseEmployeeFactory):
    def __init__(self):
        super().__init__()

    def create(self):
        manager = PermanentEmployeeManager()
        self.emp['hra'] = manager.get_hra()
        return manager
