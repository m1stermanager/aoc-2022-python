from typing import List

def parse_stack(line: str) -> List[str]:
    return [
        line[i]
        for i in range(1, len(line), 4)
    ]

def print_stacks(*stacks: List[List[str]]):
    longest_stack = max([len(s) for s in stacks])

    i = longest_stack
    printable = ""
    while i >= 0:
        for stack in stacks:
            if len(stack) > i:
                # print(i)
                printable += f"[{stack[i]}]"
            else:
                printable += "   "

            printable += " "

        i -= 1
        printable += "\n"
        # print(printable)

    print(printable)


def part1(lines: List[str]) -> int:
    stack_mode = True
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in lines:
        if line.strip() == "":
            for stack in stacks:
                stack.reverse()

            stack_mode = False
            continue

        if stack_mode:
            parsed = parse_stack(line)
            for i, parse in enumerate(parsed):
                if parse and parse.isupper():
                    stacks[i].append(parse)
        else:
            command_split = line.split(" ")
            quantity = int(command_split[1])
            start = int(command_split[3]) - 1
            end = int(command_split[5]) - 1

            tmp = stacks[start][-1*quantity:]
            tmp.reverse()
            stacks[end].extend(tmp)
            stacks[start] = stacks[start][0:len(stacks[start]) - quantity]


    ans = ""
    for stack in stacks:
        ans += stack[-1]

    return ans



def part2(lines: List[str]) -> int:
    stack_mode = True
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in lines:
        if line.strip() == "":
            for stack in stacks:
                stack.reverse()

            stack_mode = False
            continue

        if stack_mode:
            parsed = parse_stack(line)
            for i, parse in enumerate(parsed):
                if parse and parse.isupper():
                    stacks[i].append(parse)
        else:
            command_split = line.split(" ")
            quantity = int(command_split[1])
            start = int(command_split[3]) - 1
            end = int(command_split[5]) - 1

            tmp = stacks[start][-1*quantity:]

            for i in range(0, quantity, 3):
                stacks[end].extend(tmp[0+i:i+3])

            stacks[start] = stacks[start][0:len(stacks[start]) - quantity]


    ans = ""
    for stack in stacks:
        ans += stack[-1]

    return ans

def main():
    lines = None
    with open("input/day5.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()