import copy


def no_of_students_unable_to_eat_lunch(students, sandwiches):
    e_stack = []
    k = len(sandwiches) - 1
    while k >= 0:
        e_stack.append(sandwiches[k])
        k -= 1

    i = 0
    while len(students) > 0:
        print(i, students, e_stack)
        if students[0] == e_stack[-1]:
            students = students[1:]
            e_stack.pop()
        else:
            orig_students = copy.copy(students)
            k, l = (0, 1)
            while l < len(students):
                if students[k] == students[l]:
                    k += 1
                    l += 1
                else:
                    students[k], students[l] = (students[l], students[k])
                    k += 1
                    l += 1
            if orig_students == students:
                break
        i += 1
    return len(students)


students = [1, 1, 0, 0]
sandwiches = [0, 1, 0, 1]
# students = [1, 1, 1, 0, 0, 1]
# sandwiches = [1, 0, 0, 0, 1, 1]

print(no_of_students_unable_to_eat_lunch(students, sandwiches))
