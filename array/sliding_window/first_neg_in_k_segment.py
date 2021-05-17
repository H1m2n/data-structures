def first_neg_in_k_segment(arr, k):
    i = j = 0
    neg_no_i = 0
    all_neg_ele_list = []
    neg_ele_list = []
    while j < len(arr):
        if arr[j] < 0:
            all_neg_ele_list.append(arr[j])
        window_size = j - i + 1
        if window_size < k:
            j += 1
        elif window_size == k:
            # neg_ele_list.append(all_neg_ele_list[neg_no_i])
            # print(neg_ele_list)
            i += 1
            j += 1
            neg_no_i += 1
    print(all_neg_ele_list)
    return neg_ele_list


arr = [12, -1, -7, 8, -15, 30, 16, 28]
# out -> -1, -1, -7, -15, 0
first_neg_ele_list = first_neg_in_k_segment(arr, 3)
print(first_neg_ele_list)
