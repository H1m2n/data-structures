# https://leetcode.com/problems/merge-two-binary-trees/
import json
import math

from binary_search_tree.exercise1 import BST


def merge_two_array(root1, root2):
    i, j = (0, 0)
    new_tree_ele = []
    while True:
        if i < len(root1) and j < len(root2):
            new_tree_ele.append((root1[i], root2[j]))
            i += 1
            j += 1
        elif i < len(root1) and j == len(root2):
            new_tree_ele.append((root1[i], None))
            i += 1
        elif i == len(root1) and j < len(root2):
            new_tree_ele.append((None, root2[j]))
            j += 1
        elif i == len(root1) and j == len(root2):
            break
    for i, e_tuple in enumerate(new_tree_ele):
        x, y = e_tuple
        if x is not None and y is not None:
            new_tree_ele[i] = x + y
        elif x is None and y is not None:
            new_tree_ele[i] = y
        elif x is not None and y is None:
            new_tree_ele[i] = x
        elif x is None and y is None:
            new_tree_ele[i] = None
    return new_tree_ele


# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode(object):
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Tree:
    def __init__(self):
        self.root = None

    def create_tree(self, arr):
        # if parent node index is i then child node index will (2 * i+1, 2 * i + 2)
        if len(arr) == 0:
            return
        root_node = TreeNode(arr[0])
        self.root = root_node
        i = 0
        ele_queue = [root_node]
        while 2 * i + 1 <= len(arr) - 1:
            curr_node = ele_queue.pop(0)
            left_child_i = 2 * i + 1
            right_child_i = 2 * i + 2
            if left_child_i <= len(arr) - 1:
                left_child_val = arr[2 * i + 1]
                if left_child_val:
                    new_node = TreeNode(left_child_val)
                    ele_queue.append(new_node)
                    curr_node.left = new_node
            if right_child_i <= len(arr) - 1:
                right_child_val = arr[2 * i + 2]
                if right_child_val:
                    new_node = TreeNode(right_child_val)
                    ele_queue.append(new_node)
                    curr_node.right = new_node
            i += 1


def merge_two_binary_tree(root1, root2):
    ele_queue = [(None, root1, root2, None)]
    while len(ele_queue) > 0:
        parent_node, left_tree_node, right_tree_node, child_denominator = ele_queue.pop(0)
        print(parent_node, left_tree_node, right_tree_node)
        if not left_tree_node and not right_tree_node:
            # keep popping
            continue
        if left_tree_node and right_tree_node:
            ele_queue.append((left_tree_node, left_tree_node.left, right_tree_node.left, 'left'))
            ele_queue.append((left_tree_node, left_tree_node.right, right_tree_node.right, 'right'))
            left_tree_node.value = left_tree_node.value + right_tree_node.value
        elif left_tree_node and not right_tree_node:
            ele_queue.append((left_tree_node, left_tree_node.left, None, 'left'))
            ele_queue.append((left_tree_node, left_tree_node.right, None, 'right'))
            # don't need to update anything because we are updating left tree
        elif not left_tree_node and right_tree_node:
            ele_queue.append((None, None, right_tree_node.left, 'left'))
            ele_queue.append((None, None, right_tree_node.right, 'right'))
            if parent_node:
                if child_denominator == 'left':
                    parent_node.left = right_tree_node
                else:
                    parent_node.right = right_tree_node

    return root1


# root1 = [1, 3, 2, 5]
# root2 = [2, 1, 3, None, 4, None, 7]

# root1 = [1]
# root2 = [1, 2]

root1 = []
root2 = [1]

############### tree -1 ##########
tree_obj1 = Tree()
tree_obj1.create_tree(root1)

bst_obj = BST()
tree_out = bst_obj.traverse(tree_obj1.root)
json_str = json.dumps(tree_out)
print(json_str)
################## tree-2 #########
tree_obj2 = Tree()
tree_obj2.create_tree(root2)

tree_out = bst_obj.traverse(tree_obj2.root)
json_str = json.dumps(tree_out)
print(json_str)

merged_tree = merge_two_binary_tree(tree_obj1.root, tree_obj2.root)
tree_out = bst_obj.traverse(merged_tree)
json_str = json.dumps(tree_out)
print(json_str)
