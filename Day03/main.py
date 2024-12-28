import re


def part1(data: str):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return sum(int(x) * int(y) for x, y in matches)


def part2(data: str):
    parts = data.split("don't()")
    first_part, _ = parts.pop(0), parts.pop(-1)
    total = part1(first_part)
    for part in parts:
        sub_parts = part.split("do()", 1)
        if len(sub_parts) == 1:
            continue
        total += part1(sub_parts[1])
    return total


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        daily_input = f.read()

    # print(part1(daily_input))
    print(part2(daily_input))
