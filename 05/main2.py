def main():
    rules: list[tuple[int]] = []
    updates: list[list[int]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        switch: bool = True
        for line in file:
            if line == "\n":
                switch = False
                continue

            if switch:
                fom, to = map(int, line.split("|"))
                rules.append((fom, to))
            else:
                updates.append([int(_) for _ in line.split(",")])

    sorted_updates: list[list[int]] = []

    for update in updates:
        sorted_update: list[int] = []
        for value in update:
            done = True
            for index, ready_value in enumerate(sorted_update):
                if (value, ready_value) in rules:
                    sorted_update.insert(index, value)
                    done = False
                    break
            if done:
                sorted_update.append(value)
        sorted_updates.append(sorted_update)

    sumation: int = 0

    for update in sorted_updates:
        if update not in updates:
            sumation += update[len(update)//2]

    print(sumation)

if __name__ == '__main__':
    main()
