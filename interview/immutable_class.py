class SlotsFreezer:
    '''Freeze any class such that instantiated
    objects become immutable. Also use __slots__ for speed.
    '''
    __slots__ = []
    _frozen = False

    def __init__(self):
        # generate __slots__ list dynamically
        for attr_name in dir(self):
            self.__slots__.append(attr_name)
        self._frozen = True

    def __delattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__delattr__(self, *args, **kwargs)

    def __setattr__(self, *args, **kwargs):
        if self._frozen:
            raise AttributeError('This object is frozen!')
        object.__setattr__(self, *args, **kwargs)


class SlotsFreezerCar(SlotsFreezer):
    '''Contains information about a car such as make, model, etc.
    '''

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        # initialize parent class "SlotsFreezer"
        super().__init__()


slots_freezer_car = SlotsFreezerCar('Subaru', 'Crosstrek', '2018', 'Blue')
freezer_car = SlotsFreezerCar('Subaru', 'Crosstrek', '2018', 'Blue')
car = SlotsFreezerCar('Subaru', 'Crosstrek', '2018', 'Blue')
