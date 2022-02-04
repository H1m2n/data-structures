def product_of_pair(a, x):
    i, j = (0, len(a) - 1)

    while i != j:
        if a[i] * a[j] == x:
            return True
        elif a[i] * a[j] < x:
            i += 1
        else:
            j += 1
    return False


a = [1, 2, 3, 4, 5]
x = 10
print(product_of_pair(a, x))
