# Q: Given a string ‘str’ of digits and an integer ‘n’, build the lowest possible number by removing ‘n’ digits
# from the string and not changing the order of input digits.
from typing import Optional


def Q1():
    def solve(op, ip, acc):
        print(op, ip)
        if len(op) == n or len(ip) == l - n:
            acc.append(ip)
            return

        op1 = op
        op2 = op
        op1 += str(ip[0])
        solve(op1, ip[1:], acc)
        solve(op2, ip[1:], acc)

    arr = [6, 5, 4, 3, 2, 8]
    n = 2
    l = len(arr)
    acc = []
    solve("", arr, acc)
    print(acc)


# Q: Recursively Reversing a linked list
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        node = Node(value)
        if not self.head and not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def print_linked_list(self):
        arr = []
        holding_pointer = self.head
        while holding_pointer:
            arr.append(holding_pointer.val)
            holding_pointer = holding_pointer.next
        print(arr)

    def reverse_linked_list_recursively(self, holding_pointer):
        if holding_pointer.next is None:
            self.head = holding_pointer
            return

        self.reverse_linked_list_recursively(holding_pointer.next)
        curr_tail = holding_pointer.next
        curr_tail.next = holding_pointer
        holding_pointer.next = None
        self.tail = holding_pointer

    def reverse_linked_list_iteratively(self):
        if not self.head or not self.head.next:
            return
        first = self.head
        self.tail = first
        second = self.head.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first

    def retention_deletion_bk(self, m, n):
        first = None
        second = self.head
        retain_f, retain_count, del_f, del_count = (True, 0, False, 0)
        while second:
            if retain_f:
                if retain_count < m:
                    # just move ahead
                    retain_count += 1
                elif retain_count == m:
                    del_f = True
                    retain_f = False
                    retain_count = 0
            if del_f:
                if del_count < n:
                    # keep deleting
                    # temp = second.next
                    # if not temp:
                    #     first.next = None
                    #     self.tail = first
                    # else:
                    #     first.next = temp
                    #     second.next = None
                    del_count += 1

                elif del_count == n:
                    retain_f = True
                    del_f = False
                    del_count = 0
            print(retain_f, del_f)

            first = second
            second = second.next

    def retention_deletion(self, m, n):
        del_f = False
        first = None
        second = self.head
        count = 1
        while second:
            if del_f:
                temp = second.next
                if not temp:
                    first.next = None
                    self.tail = first
                else:
                    first.next = temp

            if not del_f:
                if count < m:
                    # need retention
                    count += 1
                elif count == m:
                    del_f = True
                    count = 1
                first = second  # first should not be moved in case we are deleting, that's why we are moving first only when retention is required
            else:
                if count < n:
                    count += 1
                elif count == n:
                    del_f = False
                    count = 1

            second = second.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head, tail):
        first = head
        second = head.next
        while second != tail:
            temp = second.next
            second.next = first
            first = second
            second = temp

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        orig_k = k
        holding_pointer = head
        rev_head = head
        while holding_pointer:
            k -= 1
            holding_pointer = holding_pointer.next
            if k == 0:
                self.reverse(rev_head, holding_pointer)
                k = orig_k
                rev_head = holding_pointer
        return head


obj = LinkedList()
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    obj.append(x)
obj.print_linked_list()
obj.retention_deletion(2, 2)
obj.print_linked_list()


# obj.reverse_linked_list_recursively(obj.head)
# obj.reverse_linked_list_iteratively()
# obj.print_linked_list()
# print(obj.head.__dict__, obj.tail.__dict__)

# obj1 = Solution()
# obj1.reverseKGroup(obj.head, 2)
# print(obj.print_linked_list())


def product_arr(arr, n):
    out = [1 for i in range(n)]
    start, temp = (1, 1)
    for i in range(start, n):
        out[i] = temp
        temp *= arr[i]

    start, temp = (n - 2, arr[n - 1])
    for i in range(start, -1, -1):
        out[i] *= temp
        temp *= arr[i]


product_arr([1, 2, 3, 4, 5], 5)

out = []


def flatten_arr(arr):
    if not arr:
        return
    ele = arr[0]
    arr.pop(0)
    if type(ele) is not list:
        out.append(ele)
    else:
        flatten_arr(ele)
    flatten_arr(arr)


flatten_arr([[6, 4, 7, [9, 5, 4, [2, 4, 8]]], [2, 2, 7], [9, 0, 7, [9, 3, 1, 8, 5]]])
print(out)
