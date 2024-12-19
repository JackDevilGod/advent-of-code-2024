from time import perf_counter


def recursive_remove(design: str, possible_towels: list[str]) -> bool:
    if design.strip() == "":
        return True

    for towel in possible_towels:
        if towel == design[:len(towel)]:
            if recursive_remove(design[len(towel):], possible_towels):
                return True

    return False


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
        if recursive_remove(design, possible_towels):
            amount_possible += 1

    print(amount_possible)


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
