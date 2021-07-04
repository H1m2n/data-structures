import copy


class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.e_stack = []

    def push(self, x: int) -> None:
        if self.maxSize > 0:
            self.e_stack.append(x)
            self.maxSize -= 1

    def pop(self) -> int:
        if self.maxSize == 0:
            return -1
        top = self.e_stack[-1]
        self.e_stack.pop()
        self.maxSize += 1
        return top

    def increment(self, k: int, val: int) -> None:
        tmp_stack = []
        ignore_count = len(self.e_stack) - k
        print(ignore_count, '******')
        # if ignore_count <= 0, we need to start incrementing values

        print("Before", self.e_stack.copy())
        while len(self.e_stack) > 0:
            print(ignore_count)
            x = self.e_stack[-1]
            if ignore_count <= 0:
                tmp_stack.append(x + val)
            else:
                ignore_count -= 1
                tmp_stack.append(x)
            self.e_stack.pop()

        while len(tmp_stack) > 0:
            self.e_stack.append(tmp_stack[-1])
            tmp_stack.pop()
        print("After", self.e_stack)


obj = CustomStack(3)
obj.push(1)
obj.push(2)
print(obj.e_stack)
param_2 = obj.pop()
print(param_2)
obj.push(2)
obj.push(3)
obj.push(4)
print(obj.e_stack)
obj.increment(5, 100)
print(obj.e_stack)
obj.increment(2, 100)
print(obj.e_stack)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
