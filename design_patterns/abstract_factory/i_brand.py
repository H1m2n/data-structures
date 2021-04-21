from abc import ABC, abstractmethod


class IBrand:
    @abstractmethod
    def get_brand(self):
        pass
