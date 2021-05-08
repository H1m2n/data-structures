"""
Max Heap:
input - 10  6   50  5   20  30  1
"""
import copy


class MaxHeap:
    def __init__(self):
        self.arr = [None]
        self.element_count = 1  # assumption is 1st element is already there in array even if it is not present
        self.latest_parent_index = 0
        self.latest_parent = None

    def push(self, element):
        """
        10  6   50  5   20  30  1
        for inserting every node we need to compare it with parent node. if curr node > parent node, then do swap
        1st sub tree
        1. insert 10 - [-, 10] parent node 10
        2. insert 6  - [-, 10, 6]  parent node 10
        3  insert 50 - [-, 50, 6, 10] as parent node 10 < curr node 50 then do swap. now parent is 50
          tree
                    50
                   /  \
                  6   10
        2nd subtree
        4 insert 5 - [-, 50, 6, 10, 5]. now parent is 6
        5 insert 20 - [-, 50, 20, 10, 5, 6] as parent node 6 < curr node 20 then do swap. now parent is 20
          tree
                    50
                   /  \
                  20   10
                 /  \
                5   6

        3rd subtree
        parent node is 10
        6 insert 30 - [-, 50, 20, 30, 5, 6, 10] as parent node 10 < curr node 30 the do swap, now parent is 30
        7 insert 1 - [-, 50, 20, 30, 5, 6, 10, 1]
           tree
                    50
                   /  \
                  20   30
                 /  \  / \
                5   6 10  1
        :return:
        """
        self.arr.append(element)
        self.element_count += 1
        if self.latest_parent is None:
            self.latest_parent = element
            self.latest_parent_index += 1
            return

        parent_element = self.latest_parent
        parent_index = self.latest_parent_index
        swap_check_element = element
        swap_check_index = -1
        while parent_element < swap_check_element:
            self.arr[parent_index], self.arr[swap_check_index] = (self.arr[swap_check_index], self.arr[parent_index])
            swap_check_index = parent_index
            parent_index = swap_check_index // 2
            if parent_index == 0:
                break
            parent_element = self.arr[parent_index]
            swap_check_element = self.arr[swap_check_index]

        # if self.latest_parent < element:
        #     self.arr[self.latest_parent_index], self.arr[-1] = (self.arr[-1], self.arr[self.latest_parent_index])
        #     self.latest_parent = element

        if self.element_count % 2 == 0:
            # because a smallest binary sub tree can have at-most 2 child nodes. So after we proper arranged sub tree
            # then reinitialize the state of parent node related property
            self.latest_parent_index += 1
            self.latest_parent = self.arr[self.latest_parent_index]

    def pop(self):
        """
        In heap deletion will always happen from top
        input - [None, 100, 55, 30, 50, 11, 10, 1, 5, 20, 6]
        1. 100 [None, - , 55, 30, 50, 11, 10, 1, 5, 20, 6]
        2. [None, 6, 55, 30, 50, 11, 10, 1, 5, 20, None]
            get the child nodes of parent node
            2*i, 2*i+1 - > 55, 30
            because 55 > 30
            [None, 55, 6, 30, 50, 11, 10, 1, 5, 20, None]
        3. parent node - 6, index - 2
           2*i, 2*i+1 -> arr[4], arr[5] ->
           [None, 55, 50, 30, 6, 11, 10, 1, 5, 20, None]
        4. parent node - 30, index - 3
           2*i, 2*i+1 -> arr[6], arr[7] -> 10, 1
           [None, 55, 50, 30, 6, 11, 10, 1, 5, 20, None]
        5. parent node - 6, index - 4
           2*i, 2*i+1 -> arr[8], arr[9] -> 5, 20
           [None, 55, 50, 30, 20, 11, 10, 1, 5, 6, None]
        :return:
        55
        |  \
        50  10
        | \  \
        20  11 30
        """
        popped_element = self.arr[1]
        self.arr[1] = self.arr[len(self.arr) - 1]
        self.arr[-1] = None
        parent_index = 1
        while True:
            parent_element = self.arr[parent_index]
            child_node1_index = 2 * parent_index
            child_node2_index = 2 * parent_index + 1
            if not self.arr[child_node1_index]:
                break
            if not self.arr[child_node2_index]:
                break
            if self.arr[child_node1_index] > self.arr[child_node2_index]:
                swap_check_element = self.arr[child_node1_index]
                swap_check_index = child_node1_index
            else:
                swap_check_element = self.arr[child_node2_index]
                swap_check_index = child_node2_index

            if parent_element < swap_check_element:
                self.arr[parent_index], self.arr[swap_check_index] = (
                    self.arr[swap_check_index], self.arr[parent_index])
            parent_index += 1
        self.arr = self.arr[0:-1]
        return popped_element


obj = MaxHeap()
for x in [10, 6, 50, 5, 20, 30, 1, 100, 55, 11]:
    obj.push(x)
print(obj.arr)
obj.pop()
print(obj.arr)

obj.pop()
print(obj.arr)

obj.pop()
print(obj.arr)

obj.pop()
print(obj.arr)

obj.pop()
print(obj.arr)

obj.pop()
print(obj.arr)
obj.pop()
print(obj.arr)
# [None, 50, 20, 30, 100, 6, 10, 1, 5]
# 100
# |  \
# 55  30
# | \  | \
# 50 11 10 1
# | \ \
# 5  20 6
