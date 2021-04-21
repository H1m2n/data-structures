from abc import ABC, abstractmethod


class ISystemType:
    @abstractmethod
    def get_system_type(self):
        pass
