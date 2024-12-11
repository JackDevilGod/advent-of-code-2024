from time import perf_counter


def main():
    row_stones: list[int] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            row_stones = [int(_) for _ in line.split()]

    print(row_stones)
    for instance in range(25):
        print(f"{instance + 1}/25")
        new_row: list[int] = []

        for stone in row_stones:
            if stone == 0:
                new_row.append(1)
            elif len(str(stone)) % 2 == 0:
                str_digit = str(stone)
                pivot = len(str_digit)//2
                new_row.append(int(str_digit[:pivot]))
                new_row.append(int(str_digit[pivot:]))
            else:
                new_row.append(stone * 2024)

        row_stones = new_row

    print(len(row_stones))


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
