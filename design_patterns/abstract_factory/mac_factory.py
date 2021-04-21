from design_patterns.abstract_factory.desktop import Desktop
from design_patterns.abstract_factory.i7_processor import I7Processor
from design_patterns.abstract_factory.i_brand import IBrand
from design_patterns.abstract_factory.i_computer_factory import IComputerFactory
from design_patterns.abstract_factory.i_processor import IProcessor
from design_patterns.abstract_factory.i_system_type import ISystemType
from design_patterns.abstract_factory.laptop import Laptop
from design_patterns.abstract_factory.mac import Mac


class MacDesktopFactory(IComputerFactory):
    def brand(self) -> IBrand:
        return Mac()

    def processor(self) -> IProcessor:
        return I7Processor()

    def system_type(self) -> ISystemType:
        return Desktop()


class MacLaptopFactory(MacDesktopFactory):
    def system_type(self) -> ISystemType:
        return Laptop()
