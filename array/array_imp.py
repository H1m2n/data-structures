class ArrayImp:
    def __init__(self):
        self.length = 0
        self.objects = {}

    def push(self, item):
        self.objects[self.length] = item
        self.length += 1

    def pop(self):
        last_item = self.objects[self.length - 1]
        del (self.objects[self.length - 1])
        self.length -= 1
        return last_item



obj = ArrayImp()
obj.push(10)
obj.push(20)
obj.pop()

print(obj.objects)

# obj1 = ArrayImp()
# obj1.push('hi')
# # obj.push(20)
#
# print(obj1.objects)
