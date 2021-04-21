from design_patterns.simple_factory.employee_manager import EmployeeManager


# Contract employee has medical allowance
# concrete class
class ContractEmployeeManager(EmployeeManager):
    def __init__(self):
        super().__init__()
        # self.insurance = self.get_medical_allowance()

    def get_payscale(self):
        return 1500

    def get_bonus(self):
        return 200

    def get_medical_allowance(self):
        return 200000

    def __str__(self):
        return "Contract employee"

    def __repr__(self):
        return f"ContractEmployeeManager(payscale={self.payscale}, bonus={self.bonus}, insurance={self.insurance})"
