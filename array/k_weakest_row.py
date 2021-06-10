import heapq

class Solution(object):
    def binary(self, row):
        low, high = (0, len(row) - 1)
        while low < high:
            mid_i = (low + high) // 2
            if row[mid_i] == 0:
                high = mid_i
            else:
                low = mid_i + 1
        return low

    def heapify(self):
        pass

    def kWeakestRows(self, mat, k):
        arr = []
        i = 0
        while i < len(mat):
            row = mat[i]
            low = self.binary(row)
            arr.append(low * len(mat) + i)
            i += 1

        j = len(arr) - 1
        e_stack = []
        while j >= 0:
            print(e_stack, arr[j])
            if len(e_stack) == 0:
                e_stack.append(arr[-1])
            elif len(e_stack) > 0 and e_stack[-1] >= arr[j]:
                # put greater element on top and put arr[j] element at its correct position
                tmp_stack = []
                while len(e_stack) > 0 and e_stack[-1] >= arr[j]:
                    tmp_stack.append(e_stack[-1])
                    e_stack.pop()
                e_stack.append(arr[j])
                while len(tmp_stack) > 0:
                    e_stack.append(tmp_stack[-1])
                    tmp_stack.pop()

            elif len(e_stack) > 0 and e_stack[-1] < arr[j]:
                e_stack.append(arr[j])
            j -= 1
        print(e_stack)
        return list(map(lambda x: x % len(mat), e_stack[:k]))

    def kWeakestRows_bk(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        # [
        #     [1, 0, 0],
        #     [1, 0, 0],
        #     [1, 1, 0],
        #     [1, 1, 1]
        # ]
        # i = 0, j = 1 and no of ones are equal, so return i
        # i = 2, j = 3 and sum(arr[i]) < sum(arr[j])
        #         2, 4, 1, 2, 5
        #         0  1  2  3  4

        #         (2, 0), (4, 1), (1, 2), (2, 3), (5, 4)

        #         need to create max heap
        #         [(2, 0)]
        #         [(2, 0), (4, 1)]
        #         [(2, 0), (1, 2), (4, 1)]
        #         [(2, 0), (1, 2), (2, 3)]

        arr = []
        i = 0
        while i < len(mat):
            row = mat[i]
            low = self.binary(row)
            arr.append((low, i))
            i += 1
        # because we need to find smaller number so create max heap

        j = len(arr) - 1
        e_stack = []
        while j >= 0:
            print(e_stack, arr[j][0])
            if len(e_stack) == 0:
                e_stack.append(arr[-1])
            elif len(e_stack) > 0 and e_stack[-1][0] > arr[j][0]:
                # put greater element on top and put arr[j] element at its correct position
                tmp_stack = []
                while len(e_stack) > 0 and e_stack[-1][0] > arr[j][0]:
                    tmp_stack.append(e_stack[-1])
                    e_stack.pop()
                e_stack.append(arr[j])
                while len(tmp_stack) > 0:
                    e_stack.append(tmp_stack[-1])
                    tmp_stack.pop()

            elif len(e_stack) > 0 and e_stack[-1][0] < arr[j][0]:
                e_stack.append(arr[j])

            # if len(e_stack) > k:
            #     e_stack.pop()
            j -= 1
        print(e_stack)
        i, j = (0, 1)
        res = []
        while j < len(e_stack):
            if e_stack[i][0] < e_stack[j][0]:
                res.append(e_stack[i][1])
                i += 1
                j += 1
            elif e_stack[i][0] == e_stack[j][0]:
                res.append(e_stack[i][1])
                i += 1
                j += 1
        return res[:k]


[0, 2]

mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k = 3
mat = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]
k = 3

# mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
# k = 3

# mat = [[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]]
# k = 2
obj = Solution()
print(obj.kWeakestRows(mat, k))
# 3
# 4
# 0
