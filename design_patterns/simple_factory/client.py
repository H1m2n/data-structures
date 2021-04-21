from design_patterns.simple_factory.employee_factory import EmployeeFactory

employee_type = 1
emp1 = EmployeeFactory().get_employee_manager(employee_type)
emp1.bonus = emp1.get_bonus()
emp1.payscale = emp1.get_payscale()
print(repr(emp1))

employee_type = 2
emp2 = EmployeeFactory().get_employee_manager(employee_type)
emp2.bonus = emp2.get_bonus()
emp2.payscale = emp2.get_payscale()
print(repr(emp2))
