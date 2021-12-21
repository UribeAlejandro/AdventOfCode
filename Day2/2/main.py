def run():
    with open('../data/puzzle_input.txt', 'r') as file:
        lines = [str(i.strip()) for i in file.readlines()]

    aim = 0
    depth = 0
    position = 0

    for line in lines:
        action, x = line.split(' ')[0], line.split(' ')[1]
        action = action.lower().strip()
        x = int(x)
        if action == 'forward':
            position += x
            depth += aim * x
        elif action == 'up':
            aim -= x
        elif action == 'down':
            aim += x
        else:
            pass

    return depth * position


if __name__ == "__main__":
    print(run())
