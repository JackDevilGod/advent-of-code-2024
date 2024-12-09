from copy import deepcopy
from math import prod
import time

def down_mult(element: list[int], result: int) -> bool:
    if len(element) == 1:
        return int(element[0]) == result
    else:
        copy = deepcopy(element)
        return (down_mult([copy[0] + copy[1]] + copy[2:], result) or
                down_mult([copy[0] * copy[1]] + copy[2:], result) or
                down_mult([int(str(copy[0]) + str(copy[1]))] + copy[2:], result))

def main():
    start = time.perf_counter()
    results: list[int] = []
    elements: list[list[int]] = []

    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data = [_.strip() for _ in line.split(":")]
            results.append(int(data[0]))
            elements.append([int(_) for _ in data[1].split()])
            #print(data)
            #print(results)
            #print(elements)

    tor_t: int = 0
    for i in range(len(results)):
        print(f"{i + 1}/{len(results)}")
        if down_mult(elements[i], results[i]):
            tor_t += results[i]

    print(tor_t)
    print(time.perf_counter() - start)

if __name__ == '__main__':
    main()
