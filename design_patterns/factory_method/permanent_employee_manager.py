from design_patterns.simple_factory.employee_manager import EmployeeManager


# concrete class
# permanent employee has house rent allowance
class PermanentEmployeeManager(EmployeeManager):
    def __init__(self):
        super().__init__()
        self.hra = None

    def get_payscale(self):
        return 10000

    def get_bonus(self):
        return 500

    def get_hra(self):
        return 5000

    def __str__(self):
        return "Permanent employee"

    def __repr__(self):
        return f"PermanentEmployeeManager(payscale={self.payscale}, bonus={self.bonus}, hra={self.hra})"
