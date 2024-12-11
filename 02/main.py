from time import perf_counter


def main():
    sum_safe: int = 0
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in file:
            report: list[int] = [int(i) for i in line.split()]

            if len(set(report)) != len(report):
                continue

            if report not in [sorted(report), sorted(report, reverse=True)]:
                continue

            safe: bool = True
            for index in range(0, len(report) - 1):
                if abs(report[index] - report[index + 1]) not in [1, 2, 3]:
                    safe = False
                    break

            if safe:
                sum_safe += 1

    print(sum_safe)
    print(sum_safe == 479)


if __name__ == '__main__':
    start = perf_counter()
    main()
    print(perf_counter() - start)
