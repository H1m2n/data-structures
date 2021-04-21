from design_patterns.factory_method.employee_manager_factory import EmployeeManagerFactory

emp_type = 1
emp1 = EmployeeManagerFactory().create_factory(emp_type)
emp1.apply_salary()
print(emp1.__dict__)

emp_type = 2
emp1 = EmployeeManagerFactory().create_factory(emp_type)
emp1.apply_salary()
print(emp1.__dict__)
