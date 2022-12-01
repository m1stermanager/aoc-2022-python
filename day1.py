from typing import List


def part1(lines: List[str]) -> int:
    highest_cals = 0
    current_elf = 0

    for l in lines:
        stripped = l.strip()
        if stripped == "":
            # do the whole new elf thing
            if current_elf > highest_cals:
                highest_cals = current_elf

            current_elf = 0
        else:
            current_elf += int(stripped)

    return highest_cals

def part2(lines: List[str]) -> int:
    # i can't think of anything super creative, just gonna hack this
    highest_cals_1 = 0
    highest_cals_2 = 0
    highest_cals_3 = 0

    current_elf = 0

    for l in lines:
        stripped = l.strip()
        if stripped == "":
            # do the whole new elf thing
            if current_elf > highest_cals_1:
                highest_cals_3 = highest_cals_2
                highest_cals_2 = highest_cals_1
                highest_cals_1 = current_elf
            elif current_elf > highest_cals_2:
                highest_cals_3 = highest_cals_2
                highest_cals_2 = current_elf
            elif current_elf > highest_cals_3:
                highest_cals_3 = current_elf

            current_elf = 0
        else:
            current_elf += int(stripped)

    return highest_cals_1 + highest_cals_2 + highest_cals_3
        

def main():

    lines = None
    with open("input/day1.txt", "r") as f:
        lines = f.readlines()


    print("part1:")
    print(part1(lines))

    print("part2:")
    print(part2(lines))
        

if __name__ == "__main__":
    main()