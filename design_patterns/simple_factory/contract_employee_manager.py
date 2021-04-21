from design_patterns.simple_factory.employee_manager import EmployeeManager


# concrete class
class ContractEmployeeManager(EmployeeManager):
    def __init__(self):
        super().__init__()

    def get_payscale(self):
        return 1500

    def get_bonus(self):
        return 200

    def __str__(self):
        return "Contract employee manager"

    def __repr__(self):
        return f"ContractEmployeeManager(payscale={self.payscale}, bonus={self.bonus})"
