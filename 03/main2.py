import re
from time import perf_counter


def main():
    pattern = r"(don't\(\))|(do\(\))|mul\(([0-9]+),([0-9]+)\)"
    txt: str = ""

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            txt += line

    matches = re.findall(pattern, txt)
    print(matches)

    sum: float = 0
    anabled = True
    for match in matches:
        fcommand, tcommand, x, y = match

        if fcommand == "don't()":
            anabled = False
        elif tcommand == "do()":
            anabled = True
            continue

        if anabled:
            sum += float(x) * float(y)

    print(sum)
    print(sum == 90772405)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
