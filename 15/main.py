from time import perf_counter


def main():
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            pass


if __name__ == '__main__':
    start: float = perf_counter()
    main()
    print(perf_counter() - start)
