from time import perf_counter

possible: dict[str, int] = dict()


def recursive_remove(design: str, possible_towels: list[str]) -> int:
    if design.strip() == "":
        return 1
    if design in possible.keys():
        return possible[design]

    summation: int = 0

    for towel in possible_towels:
        if design[:len(towel)] == towel:
            result = recursive_remove(design[len(towel):], possible_towels)
            if result > 0:
                summation += result
                possible[design[len(towel):]] = result

    return summation


def main():
    possible_towels: list[str] = []
    designs: list[str] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        data: list[str] = [_.removesuffix("\n") for _ in file.readlines()]
        possible_towels = [_.strip() for _ in data[0].split(",")]
        designs = data[2:]

    print(possible_towels)
    print(designs)

    possible_towels.sort(key=lambda x: len(x), reverse=True)
    amount_possible: int = 0
    for design in designs:
        print(design)
        amount_possible += recursive_remove(design, possible_towels)

    print(amount_possible)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
