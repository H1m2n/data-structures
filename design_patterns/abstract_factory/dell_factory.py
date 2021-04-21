from design_patterns.abstract_factory.dell import Dell
from design_patterns.abstract_factory.desktop import Desktop
from design_patterns.abstract_factory.i5_processor import I5Processor
from design_patterns.abstract_factory.i_brand import IBrand
from design_patterns.abstract_factory.i_computer_factory import IComputerFactory
from design_patterns.abstract_factory.i_processor import IProcessor
from design_patterns.abstract_factory.i_system_type import ISystemType
from design_patterns.abstract_factory.laptop import Laptop


class DellDesktopFactory(IComputerFactory):
    def brand(self) -> IBrand:
        return Dell()

    def processor(self) -> IProcessor:
        return I5Processor()

    def system_type(self) -> ISystemType:
        return Desktop()


class DellLaptopFactory(DellDesktopFactory):
    def system_type(self) -> ISystemType:
        return Laptop()
