# SLIDING WINDOW PROBLEM OF VARIABLE SIZE
def longest_subarray_size_of_sum_k(arr, k):
    i = j = 0
    all_candidates = []
    max_subarray_size = e_sum = 0
    while j < len(arr):
        window_size = j - i + 1
        e_sum = e_sum + arr[j]
        print(e_sum, i, j)
        if e_sum < k:
            j += 1
        elif e_sum == k:
            print(f"Condition met at i - {i} and j - {j}")
            all_candidates.append(window_size)
            max_subarray_size = max(max_subarray_size, window_size)
            j += 1
        elif e_sum > k:
            # if we found that e_sum > k, then we need to start removing element from e_sum until we got
            # e_sum <= k because we have to get other possible candidates also
            while e_sum > k:
                e_sum = e_sum - arr[i]
                i += 1
            # again before incrementing j we need to check whether now we met the condition
            if e_sum == k:
                print(f"Condition met at i - {i} and j - {j}")
                window_size = j - i + 1
                all_candidates.append(window_size)
                max_subarray_size = max(max_subarray_size, window_size)
            j += 1
    print(all_candidates)
    return max_subarray_size


# arr = [4, 1, 1, 1, 1, 1, 5]
arr = [4, 1, 1, 1, 1, 1, 3, 2]

print(longest_subarray_size_of_sum_k(arr, 5))
