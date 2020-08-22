# here we will create linked list data structures and will perform operations like inserting a node
# deleting a node, lookup, traversing(searching)

class Node:
    """
    This class represent a single node
    """

    def __init__(self, value):
        self.node = {
            'value': value,
            'next': None
        }


class LinkedList:
    # 10 --> 5 --> 16
    # linked list can be like
    # linked_list = {
    #     'head': {
    #         'value': 10,
    #         'next': {
    #             'value': 5,
    #             'next': {
    #                 'value': 16,
    #                 'next': None
    #             }
    #         }
    #     }
    # }

    def __init__(self, value):
        self.head = {
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def append(self, value):
        new_node = Node(value).node
        self.tail['next'] = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value).node
        new_node['next'] = self.head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        if index < 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return

        new_node = Node(value).node
        leader_node = self._traverse_to_leader(index - 1)
        holding_pointer = leader_node['next']
        leader_node['next'] = new_node
        new_node['next'] = holding_pointer
        self.length += 1

    def delete(self, index):
        self.length -= 1
        if index <= 0:
            # delete head node
            self.head = self.head['next']
            return

        if index > self.length:
            # delete tail node
            index = self.length - 1
            leader_node = self._traverse_to_leader(index - 1)
            leader_node['next'] = None
            self.tail = leader_node
            return

        # delete node in between linked list
        leader_node = self._traverse_to_leader(index - 1)
        unwanted_node = leader_node['next']
        leader_node['next'] = unwanted_node['next']

    def _traverse_to_leader(self, index):
        current_node = self.head
        count = 0
        while count != index:
            current_node = current_node['next']
            count += 1
        return current_node

    def print(self):
        current_node = self.head
        list_item = []
        while current_node:
            list_item.append(current_node['value'])
            current_node = current_node['next']
        return list_item


if __name__ == '__main__':
    obj = LinkedList(10)
    obj.append(5)
    obj.append(16)

    obj.prepend(1)
    obj.prepend(2)

    obj.append(20)

    obj.insert(2, 100)
    obj.insert(-100, 10)
    obj.insert(100, 10)

    obj.delete(0)
    obj.delete(100)

    print(obj.print())
