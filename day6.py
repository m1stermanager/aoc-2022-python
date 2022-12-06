from typing import List

def part1(lines: List[str]) -> int:
    ans = 0
    line = lines[0]
    for i in range(0, len(line)):
        chunk = line[i:i+4]
        if len(set(chunk)) == 4:
            ans = i+4
            break

    return ans



def part2(lines: List[str]) -> int:
    ans = 0
    line = lines[0]
    for i in range(0, len(line)):
        chunk = line[i:i+14]
        if len(set(chunk)) == 14:
            ans = i+14
            break

    return ans

def main():
    lines = None
    with open("input/day6.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()