def compress_recur(list) ->list:
    if len(list) <= 1:
        return list

    pivot = len(list)//2
    compress_left = compress_recur(list[:pivot])
    compress_right = compress_recur(list[pivot:])
    amount_left, value_left = compress_left[-1]
    amount_right, value_right = compress_right[0]
    if value_left == "." and value_right == ".":
        compress_right[0] = (amount_left + amount_right, ".")
        compress_left.pop()

    return compress_left + compress_right

def compress(list: list) -> list:
    amount_space, amount_value = list[-1]
    while amount_value == ".":
        list.pop()
        amount_space, amount_value = list[-1]

    list = compress_recur(list)

    return list


def main():
    import os
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r+") as file:
        for line in [line.removesuffix("\n") for line in file]:
            data: list[int] = [int(_) for _ in list(line)]
    # print(data)

    files: bool = True
    preprocessed_data: list[int | str] = []
    file_directory = []
    file_id: int = 0
    for block in data:
        if files:
            preprocessed_data += [(block, file_id)]
            file_directory += [(block, file_id)]
            file_id += 1
            files = False
        else:
            preprocessed_data += [(block, ".")]
            files = True
    # print(preprocessed_data)

    file_directory.reverse()
    for file in file_directory:
        print(f"{(len(file_directory) - file[1])/len(file_directory)}")

        amount_file, value_file = file
        for index in range(len(preprocessed_data)):
            amount_space, value_space = preprocessed_data[index]
            if value_space != ".":
                continue
            elif index > preprocessed_data.index(file):
                break

            if (amount_space >= amount_file):
                preprocessed_data[index] = (amount_space - amount_file, ".")

                index_file = preprocessed_data.index(file)
                preprocessed_data[index_file] = (amount_file, ".")

                preprocessed_data.insert(index, file)
                preprocessed_data = compress(preprocessed_data)
                break

    decoded_data = []
    for data in preprocessed_data:
        amount, value = data
        decoded_data += [value for _ in range(amount)]
    print(preprocessed_data)
    print(decoded_data)
    print("".join([str(_) for _ in decoded_data]))

    summation = 0
    for index, value in enumerate(decoded_data):
        if value != ".":
            summation += index * value

    print(summation)
    print(summation == 6389911791746)


if __name__ == '__main__':
    main()
