from typing import List
from collections import deque
import sys


class Solution:
    def solve_bk(self, input, width, shelf_width, height, start, dp):
        if start == len(input):
            return height

        curr_book_width = input[start][0]
        curr_book_height = input[start][1]

        new_width = width
        new_width += curr_book_width
        same_shelf = sys.maxsize
        if new_width <= shelf_width:
            # putting book in adjacent means same shelf
            if (start + 1, new_width) in dp:
                same_shelf = dp[(start + 1, new_width)]
            else:
                dp[(start + 1, new_width)] = self.solve(input, new_width, shelf_width, max(height, curr_book_height),
                                                        start + 1, dp)
                same_shelf = dp[(start + 1, new_width)]
        # putting book at next level
        if (start + 1, curr_book_width) in dp:
            next_shelf = dp[(start + 1, curr_book_width)]
        else:
            dp[(start + 1, curr_book_width)] = height + self.solve(input, curr_book_width, shelf_width,
                                                                   curr_book_height, start + 1, dp)
            next_shelf = dp[(start + 1, curr_book_width)]
        return min(same_shelf, next_shelf)

    def solve(self, input, width, shelf_width, height, start, dp):
        if start == len(input):
            return height

        if (start, width) in dp:
            return dp[(start, width)]

        curr_book_width = input[start][0]
        curr_book_height = input[start][1]

        new_width = width
        new_width += curr_book_width
        same_shelf = sys.maxsize
        # we have 2 choices to select, either we can put current book in adjacent(but if condition satisfied) or put it into next shelf,
        # for whichever process we getting min height, we need to choose that one for next processing
        if new_width <= shelf_width:
            # putting book in adjacent means same shelf
            same_shelf = self.solve(input, new_width, shelf_width, max(height, curr_book_height), start + 1, dp)
        # putting book at next level
        next_shelf = height + self.solve(input, curr_book_width, shelf_width, curr_book_height, start + 1, dp)
        dp[(start, width)] = min(same_shelf, next_shelf)
        return dp[(start, width)]

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = {}
        out = self.solve(books, 0, shelf_width, 0, 0, dp)
        return out


obj = Solution()
# books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
# shelf_width = 4

books = [[11, 83], [170, 4], [93, 80], [155, 163], [134, 118], [75, 14], [122, 192], [123, 154], [187, 29], [160, 64],
         [170, 152], [113, 179], [60, 102], [28, 187], [59, 95], [187, 97], [49, 193], [67, 126], [75, 45], [130, 160],
         [4, 102], [116, 171], [43, 170], [96, 188], [54, 15], [167, 183], [58, 158], [59, 55], [148, 183], [89, 95],
         [90, 113], [51, 49], [91, 28], [172, 103], [173, 3], [131, 78], [11, 199], [77, 200], [58, 65], [77, 30],
         [157, 58], [18, 194], [101, 148], [22, 197], [76, 181], [21, 176], [50, 45], [80, 174], [116, 198], [138, 9],
         [58, 125], [163, 102], [133, 175], [21, 39], [141, 156], [34, 185], [14, 113], [11, 34], [35, 184], [16, 132],
         [78, 147], [85, 170], [32, 149], [46, 94], [196, 3], [155, 90], [9, 114], [117, 119], [17, 157], [94, 178],
         [53, 55], [103, 142], [70, 121], [9, 141], [16, 170], [92, 137], [157, 30], [94, 82], [144, 149], [128, 160],
         [8, 147], [153, 198], [12, 22], [140, 68], [64, 172], [86, 63], [66, 158], [23, 15], [120, 99], [27, 165],
         [79, 174], [46, 19], [60, 98], [160, 172], [128, 184], [63, 172], [135, 54], [40, 4], [102, 171], [29, 125],
         [81, 9], [111, 197], [16, 90], [22, 150], [168, 126], [187, 61], [47, 190], [54, 110], [106, 102], [55, 47],
         [117, 134], [33, 107]]
shelf_width = 200
obj.minHeightShelves(books, shelf_width)
