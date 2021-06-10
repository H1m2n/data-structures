# array = [1, 3, 2, 4]
# out = [-1, -1, 3, -1]
def nearest_left_greater_element(nums):
    nearest_greatest_ele = []
    e_stack = []
    for i in range(0, len(nums), 1):
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
    return nearest_greatest_ele


# nums = [1, 3, 2, 4]
nums = [100, 80, 60, 70, 60, 75, 85]
print(nearest_left_greater_element(nums))
