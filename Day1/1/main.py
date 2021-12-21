def run():
    with open('../data/puzzle_input.txt', 'r') as file:
        lines = [int(i) for i in file.readlines()]

    count_ = 0

    for i in range(1, len(lines)):
        if lines[i] > lines[i-1]:
            count_ += 1

    return count_


if __name__ == "__main__":
    print(run())
