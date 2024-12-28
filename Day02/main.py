def part1(data: str):
    reports = data.split("\n")

    safe_reports = 0
    for report in reports:
        if not report:
            continue

        levels = list(map(int, report.split(" ")))

        is_increasing = levels[0] < levels[1]
        i = 0
        while i < len(levels) - 1:
            el1, el2 = levels[i], levels[i + 1]

            if el1 == el2:
                break

            if (is_increasing and el1 > el2) or (not is_increasing and el1 < el2) or not (1 <= abs(el1 - el2) <= 3):
                break

            i += 1
        else:
            safe_reports += 1

    return safe_reports


def part2(data: str):
    reports = data.split("\n")

    safe_reports = 0
    for report in reports:
        if not report:
            continue

        base_levels = list(map(int, report.split(" ")))

        removal_index = 0
        while removal_index < len(base_levels):
            levels = base_levels.copy()
            levels.pop(removal_index)

            is_increasing = levels[0] < levels[1]
            i = 0
            while i < len(levels) - 1:
                el1, el2 = levels[i], levels[i + 1]

                if el1 == el2:
                    break

                if (is_increasing and el1 > el2) or (not is_increasing and el1 < el2) or not (1 <= abs(el1 - el2) <= 3):
                    break

                i += 1
            else:
                safe_reports += 1
                break

            removal_index += 1

    return safe_reports


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        daily_input = f.read()

    print(part1(daily_input))
    print(part2(daily_input))
