class Solution(object):
    def get_nearest_one_to_right(self, boxes):
        i = len(boxes) - 1
        nearest_one_indices = []
        e_stack = []
        while i >= 0:
            if len(e_stack) == 0:
                nearest_one_indices.append(-1)
            elif len(e_stack) > 0 and e_stack[-1][0] == 1:
                nearest_one_indices.append(e_stack[-1][1] - i)
            elif len(e_stack) > 0 and e_stack[-1][0] == 0:
                while len(e_stack) > 0 and e_stack[-1][0] == 0:
                    e_stack.pop()
                if len(e_stack) == 0:
                    nearest_one_indices.append(-1)
                else:
                    nearest_one_indices.append(e_stack[-1][1] - i)
            e_stack.append((boxes[i], i))
            i -= 1
        nearest_one_indices.reverse()
        return nearest_one_indices

    def get_nearest_one_to_left(self, boxes):
        i = 0
        nearest_one_indices = []
        e_stack = []
        while i < len(boxes):
            if len(e_stack) == 0:
                nearest_one_indices.append(-1)
            elif len(e_stack) > 0 and e_stack[-1][0] == 1:
                nearest_one_indices.append(i - e_stack[-1][1])
            elif len(e_stack) > 0 and e_stack[-1][0] == 0:
                while len(e_stack) > 0 and e_stack[-1][0] == 0:
                    e_stack.pop()
                if len(e_stack) == 0:
                    nearest_one_indices.append(-1)
                else:
                    nearest_one_indices.append(i - e_stack[-1][1])
            e_stack.append((boxes[i], i))
            i += 1
        return nearest_one_indices

    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """

        ball_count = sum(boxes)

        # 2 + (2 + 2) + (4 + 1)
        # get the nearest 1 to right and record their index
        nearest_ones_to_right = self.get_nearest_one_to_right(boxes)
        nearest_ones_to_left = self.get_nearest_one_to_left(boxes)
        print(nearest_ones_to_right)
        print(nearest_ones_to_left)

        res = []
        for i, x in enumerate(boxes):
            if boxes[i] == 1:
                remaining_ball_count = ball_count - 1
            else:
                remaining_ball_count = ball_count
            j = i
            operation_count = 0
            while remaining_ball_count > 0:
                # compare left and right one
                # print(j, nearest_ones_to_right[j])
                right_nearest_one_dist = nearest_ones_to_right[j]
                # if right_nearest_one_dist != -1:
                operation_count += right_nearest_one_dist + (j - i)
                j = j + right_nearest_one_dist
                remaining_ball_count -= 1
            print(operation_count)
            # return


obj = Solution()
boxes = "001011"
# boxes = '111'
int_boxes = list(map(int, boxes))
obj.minOperations(int_boxes)

[0, 0, 1, 0, 1, 1]
[2, 1, 2, 1, 1, -1]
[-1, -1, -1, 1, 2, 1]

# 2 + 3 + 6 = 11
# 2 + 2 + 4 = 8
# 4 + 2


# 2 + (2 + 2) + (4 + 1) = 11
# 1 + (1 + 2) + (3 + 1) = 8
# 2 + (2 + 1) = 5
# 1 + (1) + (2) = 4
# 2 + 1 = 3
# 1 + 3 = 4
