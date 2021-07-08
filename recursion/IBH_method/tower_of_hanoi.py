# Problem: we have 3 towers, one is source, one is destination and another one is helper
# we have given some plates, in order of smaller plates is placed on top of the bigger plates.
# rule: always smaller plate is allow on top of bigger plate


steps = 0


def move(s, d, h, n):
    global steps
    steps += 1
    if n == 1:
        print(f"Moving {n}th plate from {s} to {d}")
        return
        # hypothesis step -> pick n-1 plates from source and put that into helper
    # induction step -> pick n-th plate and put that from source to destination
    move(s, h, d, n - 1)
    print(f"Moving {n}th plate from {s} to {d}")
    move(h, d, s, n - 1)


# we need to print the step and count the no of steps taken
def tower_of_hanoi(n):
    """
    s -> source id
    d -> destination id
    h -> helper tower id
    n -> no of disk
    """
    source_id, destination_id, helper_id = (1, 3, 2)
    move(source_id, destination_id, helper_id, n)


tower_of_hanoi(3)
print(steps)
