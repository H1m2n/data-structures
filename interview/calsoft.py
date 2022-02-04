# class A:

# dict = {
#     1: 10,
#     2: 20,
#     3: 50
# }
# for x in (1, 2):
#     pass
#
# (1, 101) = ['abc','xyz']


def fibo(ran):
    # 0, 1, 1, 2, 3, 5, 8
    out = []
    x, y = (0, 1)
    out.extend([x, y])
    for i in range(2, ran):
        z = x + y
        x = y
        y = z
        out.append(z)
    return out

print(fibo(10))

def func():
    return 1 + 2

a = lambda x: 1 + 2
