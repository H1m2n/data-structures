class A:
    def func(self):
        print("func() is being called")


def monkey_f(self):
    print("monkey_f() is being called")


# replacing address of "func" with "monkey_f"
A.func = monkey_f
obj = A()

# calling function "func" whose address got replaced
# with function "monkey_f()"
obj.func()
