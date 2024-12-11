import re
from time import perf_counter


def main():
    pattern = r"mul\(([0-9]+),([0-9]+)\)"
    txt: str = ""

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            txt += line

    matches = re.findall(pattern, txt)
    print(matches)

    sum: float = 0
    for match in matches:
        x, y = match
        sum += float(x) * float(y)

    print(sum)
    print(sum == 182780583)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
