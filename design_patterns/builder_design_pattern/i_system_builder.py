from abc import abstractmethod
from design_patterns.builder_design_pattern.computer_system import ComputerSystem


class ISystemBuilder:
    @abstractmethod
    def add_memory(self, memory):
        pass

    @abstractmethod
    def add_drive(self, drive_size):
        pass

    @abstractmethod
    def add_keyboard(self, type):
        """
        Used for desktop
        :param type: wired / wireless
        :return:
        """
        pass

    @abstractmethod
    def add_mouse(self, type):
        """
        Used for desktop
        :param type: wired / wireless
        :return:
        """
        pass

    @abstractmethod
    def add_touchscreen(self, enabled):
        """
        Used for laptop
        :param type: True / False
        :return:
        """
        pass

    @abstractmethod
    def get_system(self) -> ComputerSystem:
        pass
