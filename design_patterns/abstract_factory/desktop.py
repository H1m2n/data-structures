from design_patterns.abstract_factory.i_system_type import ISystemType
from design_patterns.abstract_factory.product_specifactions import System


class Desktop(ISystemType):
    def __init__(self):
        pass

    def get_system_type(self):
        return System.desktop.name
