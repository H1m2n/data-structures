# https://leetcode.com/problems/flipping-an-image/

def flip_an_image(image):
    for k, arr in enumerate(image):
        i, j = (0, len(arr) - 1)
        while i < len(arr) // 2:
            arr[i] = abs(arr[i] - 1)
            arr[j] = abs(arr[j] - 1)
            arr[i], arr[j] = (arr[j], arr[i])
            i += 1
            j -= 1
        if len(arr) % 2 != 0:
            # while reversing the middle element can't be flip, so we need to flip it here
            middle_i = len(arr) // 2
            arr[middle_i] = abs(arr[middle_i] - 1)
    return image


image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
# image = [[0, 0, 0]]

# [0, 0, 1] -> [0, 1] -> [1, 0] -> [1, 0, 0]
# [1, 0, 0]
print(flip_an_image(image))
# [1, 0, 1]
# [0, 1, 0]
