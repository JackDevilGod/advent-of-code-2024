from time import perf_counter


def main():
    row_stones: list[int] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            row_stones = [int(_) for _ in line.split()]

    count_stones: dict = {}
    for stone in set(row_stones):
        count_stones[stone] = row_stones.count(stone)

    for instance in range(75):
        print(instance)
        new_dict = {}

        for stone in count_stones.keys():
            if stone == 0:
                new_stone = [1]
            elif len(str(stone)) % 2 == 0:
                str_digit = str(stone)
                pivot = len(str_digit)//2
                new_stone = [int(str_digit[:pivot]), int(str_digit[pivot:])]
            else:
                new_stone = [stone * 2024]

            for thing in new_stone:
                if thing not in new_dict.keys():
                    new_dict[thing] = count_stones[stone]
                else:
                    new_dict[thing] += count_stones[stone]

        count_stones = new_dict

    print(sum([count_stones[key] for key in count_stones.keys()]))

if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
