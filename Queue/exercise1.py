class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            # enqueue first element
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return
        if self.first == self.last:
            self.last = None

        dequeued_ele = self.first.value
        self.first = self.first.next
        self.length -= 1
        return dequeued_ele

    def peek(self):
        return self.first


if __name__ == '__main__':
    obj = Queue()
    obj.enqueue(10)
    obj.enqueue(20)
    obj.enqueue(30)
    print(obj.peek().value)
    print(obj.dequeue())
    print(obj.dequeue())
    print(obj.dequeue())
