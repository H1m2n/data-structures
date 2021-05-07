class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, value=None):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 0

    def append(self, value):
        # O(1)
        if self.inserting_first_node(value):
            return

        node = Node(value)
        node.value = value
        self.tail.next = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        # O(1)
        if self.inserting_first_node(value):
            return

        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def insert(self, index, value):
        # O(n)
        if self.inserting_first_node(value):
            return

        if index < 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return

        node = Node(value)
        leader = self._traverse_to_leader(index - 1)
        node.next = leader.next
        leader.next = node
        self.length += 1

    def delete(self, index):
        # O(n)
        leader_node = self._traverse_to_leader(index - 1)
        unwanted_node = leader_node.next
        leader_node.next = unwanted_node.next
        self.length -= 1

    def reverse(self):
        """
        first_node = self.head
        self.tail = first_node
        second_node = first_node.next

        while(second_node)
            tmp = second_node.next
            second_node.next = first
            first_node = second_node
            second_node = tmp
        first_node.next = None
        self.head = first_node

        :return:
        """
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def _traverse_to_leader(self, index):
        current_node = self.head
        count = 0
        while count != index:
            current_node = current_node.next
            count += 1
        return current_node

    def print(self):
        current_node = self.head
        list = []
        while current_node:
            list.append(current_node.value)
            current_node = current_node.next
        return list

    def inserting_first_node(self, value):
        if self.head.value is None:
            # steps for creating first node
            self.head.value = value
            self.length += 1
            return True


if __name__ == '__main__':
    obj = SinglyLinkedList()
    obj.append(10)
    obj.append(20)
    obj.prepend(1)
    obj.insert(1, 5)
    obj.insert(1, 10)
    obj.insert(1, 10)
    obj.insert(2, 20)
    obj.insert(2, 30)
    obj.delete(2)
    obj.delete(2)
    obj.reverse()
    print(obj.print())
