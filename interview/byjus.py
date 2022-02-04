a = [5, 7, 1, 9, 10, 4, 22, 55, 86, 90]

# [1, 4, 5, 7, 9, 10, 22, 55, 86, 90]

val = 55


def binary_search():
    l = sorted(a)
    start_i = 0
    end_i = len(l) - 1
    mid_i = (end_i + start_i) // 2
    while start_i <= end_i:
        # print(start_i, end_i)
        if l[mid_i] == val:
            print("found")
            break

        if val < l[mid_i]:
            end_i = mid_i
            mid_i = (end_i + start_i) // 2
        else:
            start_i = mid_i + 1
            mid_i = (end_i + start_i) // 2


print(binary_search())
