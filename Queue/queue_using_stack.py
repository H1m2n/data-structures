# TODO
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.top = self.bottom = self.first = self.last = node
        else:
            holding_pointer = self.top
            self.top = node
            self.top.next = holding_pointer
            self.last.next = self.top
            self.last = self.top
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return

        if self.top == self.bottom == self.first == self.last:
            self.bottom = self.last = None
        dequeued_ele = self.top.value
        self.top = self.top.next
        self.first = self.top
        self.length -= 1
        return dequeued_ele

    def peek(self):
        return self.first


if __name__ == '__main__':
    obj = Queue()
    obj.enqueue(20)
    obj.enqueue(30)
    obj.enqueue(40)
    print(obj.peek().value)
    print("Dequeued - {}".format(obj.dequeue()))
    print(obj.peek().value)
    print("Dequeued - {}".format(obj.dequeue()))
    print(obj.peek().value)
