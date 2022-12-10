from typing import List
import queue

def part1(lines: List[str]) -> int:
    ans = 0

    expanded = []
    important_cycle = [19, 59, 99, 139, 179, 219]
    x = 1

    i = 0
    for line in lines:
        expanded.append(0)
        if line == "noop":
            pass
        else:
            [ _, val] = line.split(" ")
            val = int(val)
            expanded.append(val)

    for i, cycle in enumerate(expanded):
        if i in important_cycle:
            ans += x * (i+1)

        x += cycle

    print(f"x={x}")
    return ans



def part2(lines: List[str]) -> int:
    ans = 0

    expanded = []
    important_cycle = [19, 59, 99, 139, 179, 219]
    x = 1

    i = 0
    for line in lines:
        expanded.append(0)
        if line == "noop":
            pass
        else:
            [ _, val] = line.split(" ")
            val = int(val)
            expanded.append(val)

    i = 0
    for cycle in expanded:
        positions = [ x - 1, x, x + 1]

        if i in positions:
            print("#", end="")
        else:
            print(".", end="")

        # print(display)
        
        # if i in important_cycle:
        #     ans += x * (i+1)

        x += cycle
        if (i+1)%40 == 0:
            i = 0
            print("")
        else:
            i += 1

    print(f"x={x}")
    return ans

def main():
    lines = None
    with open("input/day10.txt", "r") as f:
        lines = f.readlines()

    lines = [ l.strip() for l in lines ]

    # lines = [
    #     "noop",
    #     "addx 1",
    #     "noop",
    #     "addx 1",
    #     "addx -1"
    #     # "noop",
    #     # "noop",
    # ]

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()