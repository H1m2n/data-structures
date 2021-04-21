# This factory class will compose all the related families together
from abc import abstractmethod

from design_patterns.abstract_factory.i_brand import IBrand
from design_patterns.abstract_factory.i_processor import IProcessor
from design_patterns.abstract_factory.i_system_type import ISystemType


class IComputerFactory:
    @abstractmethod
    def brand(self) -> IBrand:
        pass

    @abstractmethod
    def processor(self) -> IProcessor:
        pass

    @abstractmethod
    def system_type(self) -> ISystemType:
        pass
