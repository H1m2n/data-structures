def longest_subarry_with_max_abs_diff_less_or_equal_to_limit(nums, limit):
    i, j = (0, 0)
    max_len, min_e, max_e = (1, nums[0], nums[0])
    # for each subarray get the min and max an calculate abs diff
    while j < len(nums):
        # each time when we add an element to sub array then calculate min and max
        if nums[j] < min_e:
            min_e = nums[j]
        if nums[j] > max_e:
            max_e = nums[j]

        abs_diff = abs(min_e - max_e)
        window_size = j - i + 1
        # nums = [9, 2, 4, 7, 2, 8]
        print(f'i - {i}, j - {j}, min_e - {min_e}, max_e - {max_e}, abs diff - {abs(min_e - max_e)}')
        # print(i, j, min_e, max_e, f'abs diff - {abs(min_e - max_e)}')
        if abs_diff <= limit:
            max_len = max(max_len, window_size)
        else:
            # find out new min and max element while reducing previous sub array so that we meet with condition
            # abs_diff <= limit
            next_begin = i + 1
            min_e, max_e, change_f = (nums[next_begin], nums[next_begin], False)
            while abs_diff > limit and i <= j and not change_f:
                if nums[i] > max_e:
                    max_e = nums[i]
                    change_f = True
                if nums[i] < min_e:
                    min_e = nums[i]
                    change_f = True
                i += 1
            i = next_begin
        j += 1
    return max_len


nums = [10, 1, 2, 4, 7, 2]
nums = [9, 2, 4, 7, 2, 8]
limit = 5
print(longest_subarry_with_max_abs_diff_less_or_equal_to_limit(nums, limit))
