class School:
    def check(self, subject, marks):
        print("herer")


class Student(School):
    def __init__(self, name, age):

        self._name = name
        self._age = age
        # self.parent_obj = super().__init__()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        try:
            if age > 18:
                raise Exception
        except:
            pass

        self._age = age


obj = Student('Himanshu', 27)
# obj.parent_obj.check(10, 20)
