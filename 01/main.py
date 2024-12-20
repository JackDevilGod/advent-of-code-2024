from time import perf_counter


def main():
    left_list: list[int] = []
    right_list: list[int] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            left, right = map(int, line.split("   "))
            left_list.append(left)
            right_list.append(right)

    summation: int = 0

    for left, right in zip(sorted(left_list), sorted(right_list)):
        summation += abs(left - right)

    print(summation)
    print(summation == 2367773)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
