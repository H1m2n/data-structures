from design_patterns.abstract_factory.dell_factory import DellLaptopFactory, DellDesktopFactory
from design_patterns.abstract_factory.i_computer_factory import IComputerFactory
from design_patterns.abstract_factory.mac_factory import MacLaptopFactory, MacDesktopFactory


# business requirement:
# let say we need to allocation system to employee based on their employment type and designation
# for permanent:
#    if manage -> Apple I7 Laptop
#    if developer -> Apple I7 Desktop
#
# for contract:
#    if manage -> DELL I5 Laptop
#    if developer -> DELL I5 Desktop

class EmployeeSystemFactory:
    def __init__(self):
        pass

    def allocate_system(self, emp_type, role) -> IComputerFactory:
        if emp_type == 1:
            if role == 'manager':
                return MacLaptopFactory()
            else:
                return MacDesktopFactory()
        else:
            if role == 'manager':
                return DellLaptopFactory()
            else:
                return DellDesktopFactory()
