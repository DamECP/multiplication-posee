def large_number(n):
    return f"{n:_}".replace("_", " ")


def multiply(n1: int, n2: int):
    steps = []
    # the biggest number is at the top
    value1, value2 = (n2, n1) if n2 > n1 else (n1, n2)
    power = 1

    # steps results
    for i in reversed(str(value2)):
        result = int(i) * value1 * power
        steps.append(result)
        # *10 for each step
        power *= 10

    final_result = sum(steps)

    # design
    width = len(large_number(final_result)) + 2

    print(f"{large_number(value1):>{width}}")
    print(f"x {large_number(value2):>{width -2}}")
    print("─" * width)

    if len(steps) > 1:
        print(f"{large_number(steps[0]):>{width}}")
        for i in steps[1:]:
            print(f"+ {large_number(i):>{width -2}}")
        print("─" * width)

    print(f"{large_number(final_result):>{width}}")


def ask_for_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Integer only")


while True:
    n1 = ask_for_number("First value (0 to quit) : ")
    if n1 == 0:
        break
    n2 = ask_for_number("Second value (0 to quit) : ")
    print()
    if n2 == 0:
        break

    multiply(n1, n2)
    print()
