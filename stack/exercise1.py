class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = node
            self.bottom = node
        else:
            holding_pointer = self.top
            self.top = node
            self.top.next = holding_pointer
        self.length += 1

    def pop(self):
        if self.length == 0:
            return
        if self.top == self.bottom:
            self.bottom = None
        popped_value = self.top.value
        self.top = self.top.next
        self.length -= 1
        return popped_value

    def peek(self):
        return self.top


if __name__ == '__main__':
    obj = Stack()
    obj.push('google')
    obj.push('udemy')
    obj.push('linkedin')
    obj.pop()
    obj.pop()
    obj.pop()
    print(obj.peek())
