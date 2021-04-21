from design_patterns.builder_design_pattern.computer_system import ComputerSystem
from design_patterns.builder_design_pattern.i_system_builder import ISystemBuilder


class LaptopBuilder(ISystemBuilder):
    def __init__(self):
        self.laptop_system = ComputerSystem()

    def add_memory(self, memory):
        self.laptop_system.memory = memory
        return self

    def add_drive(self, drive_size):
        self.laptop_system.hdd_Size = drive_size
        return self

    def add_keyboard(self, type):
        return self

    def add_mouse(self, type):
        return self

    def add_touchscreen(self, enabled):
        self.laptop_system.is_touch_screen = enabled
        return self

    def get_system(self) -> ComputerSystem:
        return self.laptop_system
