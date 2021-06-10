# Sample brute force approach
# for i = 0; i < n-1; i++ {
#   ele_found_f = 0
#   for j = i+1; j < n; j++ {
#       if arr[j] > arr[i]:
#         nearest_greatest_ele.append(arr[j])
#         ele_found_f = 1
#         break
#   }
#   if ele_found_f == 0:
#       nearest_greatest_ele.append(-1)
# }

# Approach: As we need to find greater element to right of the current element
# So in stack approach we need to traverse from right to left because right element should be present in stack for
# making decision on that
# arr = [1, 3, 2, 4]
# for i = 3, stack will be empty, so the value will be -1 push -1 to an array and push 3 to stack
# for i = 2, arr[i] i:e 2 < 4, so  push 4 to an array, and push 2 in stack
# for i = 1, compare 3 with top of stack, as 3 > 2, then pop 2 from stack, and we need to do this comparision until
# we don't get element or stack is empty
def nearest_right_greater_element(nums):
    nearest_greatest_ele = []
    e_stack = []
    for i in range(len(nums) - 1, -1, -1):
        if len(e_stack) == 0:
            # if stack is empty, then push -1
            nearest_greatest_ele.append(-1)
        elif len(e_stack) > 0 and nums[i] < e_stack[-1]:
            # if top of the stack is > than arr[i], then push top of stack
            nearest_greatest_ele.append(e_stack[-1])
        elif len(e_stack) > 0 and nums[i] > e_stack[-1]:
            # if top of stack is < arr[i], then pop until top of stack is > arr[i] or stack is empty
            while len(e_stack) > 0 and nums[i] > e_stack[-1]:
                e_stack.pop()

            # check if stack is empty then push -1 otherwise we got a greater element then push that into array
            if len(e_stack) == 0:
                nearest_greatest_ele.append(-1)
            else:
                nearest_greatest_ele.append(e_stack[-1])
        # at last push arr[i] to stack for comparing rest of the elements
        e_stack.append(nums[i])
    nearest_greatest_ele.reverse()
    return nearest_greatest_ele


nums = [1, 3, 2, 4]
nearest_right_greater_element(nums)
