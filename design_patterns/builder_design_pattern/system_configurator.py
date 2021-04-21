from design_patterns.builder_design_pattern.i_system_builder import ISystemBuilder


class SystemConfigurator:
    def __init__(self):
        pass

    def configure_system(self, i_system_builder: ISystemBuilder, system_config: dict):
        """
        We can configure a system here step by step, system config we can get from outside as a dictionary
        :param i_system_builder:
        :param system_config:
        :return:
        """
        i_system_builder.add_drive(system_config.get('drive')) \
            .add_memory(system_config.get('memory')) \
            .add_keyboard(system_config.get('keyboard_type')) \
            .add_mouse(system_config.get('mouse_type')) \
            .add_touchscreen(system_config.get('touchscreen_enabled'))
