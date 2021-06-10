# Problem: We need to add min function to stack,
# how it should work? whenever we pop something from stack, then now we should able to get next min element


class Stack:
    def __init__(self):
        self.e_stack = []
        self.min_stack = []

    def push(self, e):
        self.e_stack.append(e)
        if len(self.min_stack) == 0:
            self.min_stack.append(e)
        else:
            min_e = self.min_stack[-1]
            if e <= min_e:
                self.min_stack.append(e)

    def pop(self):
        pop_e = self.e_stack[-1]
        min_e = self.min_stack[-1]
        if pop_e == min_e:
            self.min_stack.pop()
        self.e_stack.pop()

    def get_min(self):
        if len(self.min_stack) == 0:
            return None
        return self.min_stack[-1]


arr = [18, 19, 29, 15, 15, 16]
obj = Stack()
obj.push(18)
obj.push(19)
obj.push(29)
# obj.pop()
# obj.pop()
# obj.pop()
obj.push(15)
obj.push(15)
# obj.pop()
# obj.pop()
obj.push(16)
# obj.pop()
# obj.pop()
print(obj.e_stack, obj.min_stack)
