from abc import ABC, abstractmethod


class IProcessor:
    @abstractmethod
    def get_processor(self):
        pass
