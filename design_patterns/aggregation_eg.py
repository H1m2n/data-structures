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
        self.heartValves = heartValves  # Aggregation

    def display(self):
        print("First Name: ", self.fname)
        print("Last Name: ", self.lname)
        print("Address: ", self.address)
        print("No of Healthy Valves: ", self.heartValves.display())


hv = Heart(4)
p = Person("Adam", "Lee", "555 wso blvd", hv)
p.display()