# eg:      5
#        /   \
#       3     7
#      / \   /  \
#     1   4  6   8
import json


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

    def bfs_traversal(self):
        data = []
        queue = [self.root]
        # print(queue.pop(0))
        while len(queue) > 0:
            current_node = queue.pop(0)
            data.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return data

    def remove(self, value):
        if self.root is None:
            return
        else:
            curr_node = self.root
            parent_node = None
            while curr_node:
                if curr_node.value == value:
                    # check if curr_node node is a leaf node
                    if curr_node.left is None and curr_node.right is None:
                        # remove link from parent node of curr_node
                        if parent_node.left.value == curr_node.value:
                            parent_node.left = None
                        elif parent_node.right.value == curr_node.value:
                            parent_node.right = None
                    elif curr_node.left is None and curr_node.right:
                        # if curr node's left tree is not available but right tree is available then attach to
                        # left or right side of parent's node according to below condition
                        if parent_node.value > curr_node.value:
                            parent_node.left = curr_node.right
                        else:
                            parent_node.right = curr_node.right
                    elif curr_node.right is None and curr_node.left:
                        # if curr node's left tree is not available but right tree is available then attach to
                        # left or right side of parent's node according to below condition
                        if parent_node.value > curr_node.value:
                            parent_node.left = curr_node.left
                        else:
                            parent_node.right = curr_node.left
                    else:
                        if curr_node.right.left is None:
                            if parent_node.value > curr_node.value:
                                # perform operation on left
                                parent_node.left = curr_node.right
                                parent_node.left.left = curr_node.left
                            else:
                                # perform operation on right
                                parent_node.right = curr_node.right
                                parent_node.right.left = curr_node.left
                        else:
                            parent_of_left_most_node = curr_node.right
                            left_most_node = curr_node.right.left
                            while left_most_node.left:
                                parent_of_left_most_node = left_most_node
                                left_most_node = left_most_node.left
                            parent_of_left_most_node.left = left_most_node.right
                            parent_node.right = left_most_node
                            left_most_node.left = curr_node.left
                            left_most_node.right = curr_node.right

                parent_node = curr_node
                if value < curr_node.value:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

    def is_valid_BST(self):
        data = []
        queue = [self.root]
        # print(queue.pop(0))
        while len(queue) > 0:
            current_node = queue.pop(0)
            data.append(current_node.value)
            if current_node.left:
                if current_node.left.value > current_node.value:
                    return False
                queue.append(current_node.left)
            if current_node.right:
                if current_node.right.value < current_node.value:
                    return False
                queue.append(current_node.right)
        print(data)
        return True

    def traverse(self, node):
        tree = {'value': node.value}
        tree['left'] = None if node.left is None else self.traverse(node.left)
        tree['right'] = None if node.right is None else self.traverse(node.right)
        return tree


if __name__ == '__main__':
    obj = BST()
    obj.insert(5)
    obj.insert(3)
    obj.insert(7)
    obj.insert(1)
    obj.insert(4)
    obj.insert(6)
    obj.insert(10)
    obj.insert(9)
    obj.insert(15)
    obj.insert(8)
    obj.insert(16)
    obj.insert(8.5)
    tree_out = obj.traverse(obj.root)
    json_str = json.dumps(tree_out)
    print(json_str)

    # obj.remove(3)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    #
    # # print(obj.lookup(10))
    # # print(obj.is_valid_BST())
    # obj.remove(10)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    #
    # obj.insert(0.5)
    # obj.remove(4)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    #
    # obj.remove(7)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    # obj.remove(8)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    # obj.remove(9)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
    # obj.remove(15)
    # tree_out = obj.traverse(obj.root)
    # json_str = json.dumps(tree_out)
    # print(json_str)
