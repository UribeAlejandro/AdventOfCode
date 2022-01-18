def run():
    with open('../data/puzzle_input.txt', 'r') as file:
        lines = [str(i.strip()) for i in file.readlines()]

    seq_dict = {i:'' for i in range(0,len(lines[0]))}

    for line in lines:
        for i, char in enumerate(line):
            seq_dict[i] += char

    return seq_dict


def int2bin(n):
    return int2bin(n >> 1) + [n & 1] if n > 1 else [1]


if __name__ == "__main__":
    print(run())
