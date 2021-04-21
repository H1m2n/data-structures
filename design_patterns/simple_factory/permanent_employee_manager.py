from design_patterns.simple_factory.employee_manager import EmployeeManager


# concrete class
class PermanentEmployeeManager(EmployeeManager):
    def __init__(self):
        super().__init__()

    def get_payscale(self):
        return 10000

    def get_bonus(self):
        return 500

    def __str__(self):
        return "Permanent employee"

    def __repr__(self):
        return f"PermanentEmployeeManager(payscale={self.payscale}, bonus={self.bonus})"
