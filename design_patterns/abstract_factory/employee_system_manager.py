class EmployeeSystemManger:

    def __init__(self, i_computer_factory):
        self._i_computer_factory = i_computer_factory

    def get_system_details(self):
        i_brand = self._i_computer_factory.brand()
        i_system_type = self._i_computer_factory.system_type()
        i_processor = self._i_computer_factory.processor()

        return f"{i_brand.get_brand()} {i_system_type.get_system_type()} {i_processor.get_processor()}"
