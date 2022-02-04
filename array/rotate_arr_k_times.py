def reversing_approach(nums, k):
    def reverse(start_i, end_i, nums):
        while start_i <= end_i:
            nums[start_i], nums[end_i] = (nums[end_i], nums[start_i])
            start_i += 1
            end_i -= 1

    n = len(nums)
    k = k % n  # to ensure if k > n, k should lie in between range of 1 to n
    reverse(0, n - k - 1, nums)
    reverse(n - k, n - 1, nums)
    reverse(0, n - 1, nums)


def rotate_arr_k_times(nums, k):
    # Time complexity O(n)
    # Space Complexity O(n)

    e_stack = []
    i = len(nums) - 1
    while i >= 0:
        e_stack.append(nums[i])
        i -= 1

    i = 0
    while len(e_stack) > 0:
        final_i = (i + k) % len(nums)
        nums[final_i] = e_stack[-1]
        e_stack.pop()
        i += 1


nums = [1, 2, 3, 4, 5]
k = 3
# rotate_arr_k_times(nums, k)
reversing_approach(nums, k)


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LRU:
    def __init__(self):
        self.root = None
        self.head = None
        self.tail = None

    def find_and_delete_node(self, val):
        first = None
        holding_pointer = self.head
        while holding_pointer:
            if holding_pointer.val == val:
                break
            first = holding_pointer
            holding_pointer = holding_pointer.next
        if holding_pointer:
            if first is None:
                self.head = holding_pointer.next
            else:
                first.next = holding_pointer.next

    def LRU_cache(self, arr):
        ele_dict = {}
        for x in arr:
            node = Node(x)
            if x not in ele_dict:
                ele_dict[x] = 0
                if self.root is None:
                    self.root = node
                    self.head = node
                    self.tail = node
                else:
                    self.tail.next = node
                    self.tail = node
            else:
                self.find_and_delete_node(x)
                self.tail.next = node
                self.tail = node
        print(ele_dict)

    def print(self):
        current_node = self.head
        list = []
        while current_node:
            list.append(current_node.val)
            current_node = current_node.next
        return list


obj = LRU()
arr = [1, 4, 1, 3]
obj.LRU_cache(arr)
print(obj.print())
