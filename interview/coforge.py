l = [100, 91, 0, -1, 22]


# [91, 100]
# [0, 100]
# [-1, 100]
# [22, 100]

def bubble_sort(l):
    for i, x in enumerate(l):
        for j, y in enumerate(l):
            if x < y:
                l[i], l[j] = (l[j], l[i])

    print(l)


bubble_sort(l)

# l = [10, 20]
# l[0], l[1] = (l[1], l[0])
# print(l)

print([x for x in range(1, 51) if x % 2 == 0])
