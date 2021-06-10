# Note: This problem is the variant of MAH(maximum area histogram)
# Approach: convert 2D array into 1D array and then for 1D array we know how to calculate MAH.
# for eg:
# from stack.maximum_area_histogram import maximum_area_histogram

arr = [
    [0, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 0, 0]
]
# so above array represent matrix of 4 * 4
# Step 1: 2D to 1D
#   1. histogram of 1 * 4 = [0, 1, 1, 0]
#   2. histogram of 2 * 4 = [1, 2, 2, 1]
#   3. histogram of 3 * 4 = [2, 3, 3, 2]
#   4. histogram of 4 * 4 = [3, 4, 0, 0]  ---> histogram means a building, because at arr[4][3] and arr[4][4] == 0 so
#                                              building height is 0 as a building can be formed on continuous blocks
# answer will be = max(MAH1, MAH2, MAH3, MAH4)

histogram_dict = {}
for i, row in enumerate(arr):
    if i == 0:
        histogram_dict[f"{i + 1} * 4"] = row
    else:
        histogram_blocks = []
        for j, col in enumerate(row):
            if col == 0:
                histogram_blocks.append(0)
            else:
                prev_histogram_block = histogram_dict[f"{i} * 4"]
                histogram_blocks.append(prev_histogram_block[j] + col)
        histogram_dict[f"{i + 1} * 4"] = histogram_blocks
print(histogram_dict)

max_area = 0
for k, histogram in histogram_dict.items():
    print(histogram)
    # max_area = max(max_area, maximum_area_histogram(histogram))
print(max_area)
