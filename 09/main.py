def main():
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data: list[int] = [int(_) for _ in list(line)]

    # print(data)

    files: bool = True
    preprocessed_data: list[int | str] = []
    file_id: int = 0
    for block in data:
        if files:
            preprocessed_data += [file_id for _ in range(block)]
            file_id += 1
            files = False
        else:
            preprocessed_data += ["." for _ in range(block)]
            files = True

    # print(preprocessed_data)
    summation: int = 0
    index = 0
    while index < len(preprocessed_data):
        if "." in preprocessed_data:
            while preprocessed_data[-1] == ".":
                preprocessed_data.pop()

            free_index = preprocessed_data.index(".")
            preprocessed_data[free_index] = preprocessed_data.pop()

        summation += index * preprocessed_data[index]
        index += 1

    print(summation)
    print(summation == 6356833654075)


if __name__ == '__main__':
    main()
