from design_patterns.builder_design_pattern.desktop_builder import DesktopBuilder
from design_patterns.builder_design_pattern.laptop_builder import LaptopBuilder
from design_patterns.builder_design_pattern.system_configurator import SystemConfigurator


system_builder = LaptopBuilder()
sys_specification = {
    'memory': '8 GB',
    'drive': '500 GB',
    'touchscreen_enabled': True
}
SystemConfigurator().configure_system(system_builder, sys_specification)
system = system_builder.get_system()

print(system.__dict__)

system_builder = DesktopBuilder()
sys_specification = {
    'memory': '8 GB',
    'drive': '1 TB',
    'keyboard_type': 'wireless',
    'mouse_type': 'wireless'
}
SystemConfigurator().configure_system(system_builder, sys_specification)
system = system_builder.get_system()

print(system.__dict__)
