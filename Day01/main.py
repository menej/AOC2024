from collections import Counter


def part1(data: str):
    left = []
    right = []

    for line in data.split("\n"):
        left.append(int(line.split(" ")[0]))
        right.append(int(line.split(" ")[-1]))

    left.sort()
    right.sort()

    return sum(abs(x - y) for x, y in zip(left, right))


def part2(data: str):
    left = []
    right = []

    for line in data.split("\n"):
        left.append(int(line.split(" ")[0]))
        right.append(int(line.split(" ")[-1]))

    left.sort()
    right.sort()

    c_left = Counter(left)
    c_right = Counter(right)

    return sum(repeat * num * c_right[num] for num, repeat in c_left.items() if num in c_right)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        daily_input = f.read()

    print(part1(daily_input))
    print(part2(daily_input))
