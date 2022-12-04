from typing import List

def part1(lines: List[str]) -> int:
    ans = 0

    for line in lines:
        [ r1, r2 ] = line.split(",")
        r1min, r1max = r1.split("-")
        r2min, r2max = r2.split("-")

        r1min = int(r1min)
        r1max = int(r1max)
        r2min = int(r2min)
        r2max = int(r2max)

        if r1min >= r2min and r1min <= r2max and r1max <= r2max:
            ans += 1
        elif r2min >= r1min and r2min <= r1max and r2max <= r1max:
            ans += 1

    return ans



def part2(lines: List[str]) -> int:
    ans = 0

    for line in lines:
        [ r1, r2 ] = line.split(",")
        r1min, r1max = r1.split("-")
        r2min, r2max = r2.split("-")

        r1min = int(r1min)
        r1max = int(r1max)
        r2min = int(r2min)
        r2max = int(r2max)

        range1 = set(range(r1min, r1max + 1))
        range2 = set(range(r2min, r2max + 1))

        if len(range1 & range2) > 0:
            ans += 1

    return ans

def main():
    lines = None
    with open("input/day4.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()