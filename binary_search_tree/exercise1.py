# eg:      5
#        /   \
#       3     7
#      / \   /  \
#     1   4  6   8
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return
        current_node = self.root

        while True:
            if value < current_node.value:
                if not current_node.left:
                    current_node.left = node
                    return
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = node
                    return
                current_node = current_node.right

    def lookup(self, value):
        if not self.root:
            return False
        current_node = self.root
        while current_node:
            if current_node.value == value:
                return True
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right


if __name__ == '__main__':
    obj = BST()
    obj.insert(5)
    obj.insert(3)
    obj.insert(7)
    obj.insert(1)
    obj.insert(4)
    obj.insert(6)
    obj.insert(8)
    print(obj.lookup(8))
