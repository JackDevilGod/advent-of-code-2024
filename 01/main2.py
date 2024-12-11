from time import perf_counter


def main():
    left_list: list = []
    right_list: list = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            left, right = map(int, line.split("   "))
            left_list.append(left)
            right_list.append(right)

    summation: float = 0
    for num in sorted(left_list):
        summation += num * right_list.count(num)

    print(summation)
    print(summation == 21271939)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
