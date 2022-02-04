# '{[((}))' (not valid)
# '{[(({}))]}' ( valid)
# '{[{}(({}))]}' ( valid)
#

def lookup_logic(e_stack, open_brac):
    popped_e = []
    while len(e_stack) > 0 and e_stack[-1] != open_brac:
        popped_e.append(e_stack[-1])
        e_stack.pop()
    if len(e_stack) == 0:
        pass
    else:
        e_stack.pop()

    e_stack.extend(popped_e)


def bracket_check(pattern):
    e_stack = []

    i = 0
    while i < len(pattern):
        if pattern[i] in ['{', '[', '(']:
            e_stack.append(pattern[i])
        elif pattern[i] == ')':
            lookup_logic(e_stack, '(')
        elif pattern[i] == '}':
            lookup_logic(e_stack, '{')
        elif pattern[i] == ']':
            lookup_logic(e_stack, '[')

        i += 1
    # print(e_stack)
    return len(e_stack) == 0


print(bracket_check('{[((}))'))
print(bracket_check('{[{}(({}))]}'))
print(bracket_check('{[{}(({}))]}'))
print(bracket_check('}}{{'))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"name - {self.name}, age - {str(self.age)}"


p1 = Person('Himanshu', 27)
p2 = Person('Shashank', 24)
p3 = Person('Amit', 40)


def custom_sort(x):
    return x.age


out = sorted([p1, p2, p3], key=lambda x: custom_sort(x))
print(out)


def iterate():
    for x in range(1, 10):
        yield x

    for x in range(10, 20):
        yield x


print(type(iterate()))

obj = iter(iterate())
print(next(obj))
print(next(obj))

# for x in iterate():
#     print(x, '********')
