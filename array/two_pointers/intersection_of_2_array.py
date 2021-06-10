# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# nums1 = [4,5,9]
# nums2 = [4,4,8,9,9]
def intersection_of_2_array(nums1: list, nums2: list):
    intersection_list = []
    nums1.sort()
    nums2.sort()
    # if arr[j] > arr[i], so to balance we need to increase j
    # if arr[j] < arr[i], so to balance we need to increase j
    i, j = (0, 0)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            intersection_list.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            i += 1
    return intersection_list


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection_of_2_array([4, 5, 9], [4, 4, 8, 9, 9]))
print(intersection_of_2_array(nums1, nums2))
