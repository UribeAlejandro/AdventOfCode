def run():
    with open('../data/puzzle_input.txt', 'r') as file:
        lines = [int(i) for i in file.readlines()]

    count_ = -1
    sum_prev = 0

    for i in range(0, len(lines)-2):
        sum_next = sum(lines[i:i+3])
        if sum_prev < sum_next:
            count_ += 1
        sum_prev = sum_next

    return count_


if __name__ == "__main__":
    print(run())
