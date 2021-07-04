# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_left_and_right_prefix(self, arr, max_e, idx):
        left_prefix, right_prefix = ([], [])
        for i in range(idx):
            left_prefix.append(arr[i])

        for i in range(idx + 1, len(arr)):
            right_prefix.append(arr[i])
        return [left_prefix, right_prefix]

    def get_max_ele(self, arr):
        max_e, idx = (arr[0], 0)
        for i, x in enumerate(arr):
            if max_e < x:
                max_e = x
                idx = i
        return [max_e, idx]

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_e, idx = self.get_max_ele(nums)
        left_prefix, right_prefix = self.get_left_and_right_prefix(nums, max_e, idx)

        parent_node = TreeNode(max_e)
        left_child = self.constructMaximumBinaryTree(left_prefix)
        parent_node.left = left_child

        right_child = self.constructMaximumBinaryTree(right_prefix)
        parent_node.right = right_child
        return parent_node

    def traverse(self, node):
        tree = {'val': node.val}
        tree['left'] = None if node.left is None else self.traverse(node.left)
        tree['right'] = None if node.right is None else self.traverse(node.right)
        return tree


obj = Solution()
nums = [3, 2, 1, 6, 0, 5]
node = obj.constructMaximumBinaryTree(nums)

print(obj.traverse(node))
# print(node.__dict__)
