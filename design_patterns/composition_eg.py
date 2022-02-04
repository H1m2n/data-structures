class Heart:
    def __init__(self, heartValves):
        self.heartValves = heartValves

    def display(self):
        return self.heartValves


class Person:
    def __init__(self, fname, lname, address, heartValves):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.heartValves = heartValves
        self.heartObject = Heart(self.heartValves)  # Composition

    def display(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Address: ", self.address)
        print("No of Heart Valves: ", self.heartObject.display())


p = Person("Adam", "syn", "876 Zyx Ln", 4)
p.display()
