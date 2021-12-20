def run():
    with open('../data/puzzle_input.txt', 'r') as file:
        lines = [str(i.strip()) for i in file.readlines()]

    print(lines[:][1])
    top_bits = len(lines)
    n_bits = len(lines[0])
    seq_dict = {}

    for i in range(0, n_bits):
        seq_dict[i] = lines[:][i]

    return seq_dict
def int2bin(n):
    return int2bin(n >> 1) + [n & 1] if n > 1 else [1]


if __name__ == "__main__":
    print(run())
