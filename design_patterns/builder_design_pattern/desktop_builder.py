from design_patterns.builder_design_pattern.computer_system import ComputerSystem
from design_patterns.builder_design_pattern.i_system_builder import ISystemBuilder


class DesktopBuilder(ISystemBuilder):
    def __init__(self):
        self.desktop_system = ComputerSystem()

    def add_memory(self, memory):
        self.desktop_system.memory = memory
        return self

    def add_drive(self, drive_size):
        self.desktop_system.hdd_Size = drive_size
        return self

    def add_keyboard(self, type):
        self.desktop_system.keyboard_type = type
        return self

    def add_mouse(self, type):
        self.desktop_system.mouse_type = type
        return self

    def add_touchscreen(self, enabled):
        return self

    def get_system(self) -> ComputerSystem:
        return self.desktop_system
