from time import perf_counter


def main():
    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        inp: str = file.readline()
        while inp != "\n":
            fom, to = map(int, inp.split("|"))
            rules.append((fom, to))
            inp = file.readline()

        inp = file.readline()
        while inp != "":
            updates.append([int(_) for _ in inp.split(",")])
            inp = file.readline()

    sorted_updates: list[list[int]] = []

    for update in updates:
        sorted_update: list[int] = []
        for value in update:
            for index, ready_value in enumerate(sorted_update):
                if (value, ready_value) in rules:
                    sorted_update.insert(index, value)
                    break

            sorted_update.append(value)
        sorted_updates.append(sorted_update)

    summation: int = 0

    for update in sorted_updates:
        if update in updates:
            summation += update[len(update)//2]

    print(summation)
    print(summation == 5651)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
