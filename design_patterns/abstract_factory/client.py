from design_patterns.abstract_factory.employee_system_factory import EmployeeSystemFactory
from design_patterns.abstract_factory.employee_system_manager import EmployeeSystemManger

emp_type = 1
role = 'manager'

i_computer_factory = EmployeeSystemFactory().allocate_system(emp_type, role)
system_details = EmployeeSystemManger(i_computer_factory).get_system_details()
print(system_details)

emp_type = 1
role = 'developer'

i_computer_factory = EmployeeSystemFactory().allocate_system(emp_type, role)
system_details = EmployeeSystemManger(i_computer_factory).get_system_details()
print(system_details)

emp_type = 2
role = 'manager'

i_computer_factory = EmployeeSystemFactory().allocate_system(emp_type, role)
system_details = EmployeeSystemManger(i_computer_factory).get_system_details()
print(system_details)

emp_type = 2
role = 'developer'

i_computer_factory = EmployeeSystemFactory().allocate_system(emp_type, role)
system_details = EmployeeSystemManger(i_computer_factory).get_system_details()
print(system_details)
