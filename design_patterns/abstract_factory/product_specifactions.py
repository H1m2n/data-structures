import enum


class Brand(enum.Enum):
    mac = 1
    dell = 2


class System(enum.Enum):
    laptop = 1
    desktop = 2


class Processor(enum.Enum):
    I7 = 1
    I5 = 2


# print(Brand.apple.name)
