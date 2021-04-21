from abc import ABC, abstractmethod


# interface class
class EmployeeManager:
    def __init__(self):
        self.payscale = None
        self.bonus = None

    @abstractmethod
    def get_payscale(self):
        raise NotImplementedError

    @abstractmethod
    def get_bonus(self):
        raise NotImplementedError
