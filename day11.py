from decimal import Decimal
from typing import List
from dataclasses import dataclass

@dataclass
class Monkey:
    items: List[int]
    op: callable
    test_num: int
    test_true: int
    test_false: int

    inspections: int = 0


def get_op(line: str, compressor: int = None):
    if "*" in line:
        val = line.split("*")[1].strip()
        if val == "old":
            val = None
        else:
            val = int(val)

        return lambda old: old * (val or old)

    val = line.split("+")[1].strip()
    if val == "old":
        val = None
    else:
        val = int(val)

    return lambda old: old + (val or old)

def parse_monkey(lines: List[str], compressor: int = None) -> Monkey:
    items = [ int(x.strip()) for x in lines[1].split(":")[1].split(",") ]
    op = get_op(lines[2], compressor)
    div_by = int(lines[3].split(" ")[-1])
    test_true = int(lines[4].split(" ")[-1])
    test_false = int(lines[5].split(" ")[-1])

    return Monkey(items, op, div_by, test_true, test_false)



def part1(lines: List[str]) -> int:
    ans = 0
    monkeys: List[Monkey] = []

    for i in range(0, len(lines), 7):
        m = parse_monkey(lines[i:i+7])
        monkeys.append(m)

    for _ in range(0, 20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections = monkey.inspections + 1

                worry = monkey.op(item)
                worry = worry//3
                if (worry % monkey.test_num) == 0:
                    monkeys[monkey.test_true].items.append(worry)
                else:
                    monkeys[monkey.test_false].items.append(worry)
            
            monkey.items = []

    monkeys.sort(key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections



def part2(lines: List[str]) -> int:
    monkeys: List[Monkey] = []
    compressor = 1000000000

    for i in range(0, len(lines), 7):
        m = parse_monkey(lines[i:i+7], compressor)
        monkeys.append(m)

    for _ in range(0, 20):
        for monkey in monkeys:
            for item in monkey.items:
                monkey.inspections = monkey.inspections + 1

                worry = monkey.op(item)
                worry = worry//3
                if (worry % monkey.test_num) == 0:
                    monkeys[monkey.test_true].items.append(worry)
                else:
                    monkeys[monkey.test_false].items.append(worry)
            
            monkey.items = []

    monkeys.sort(key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections

def main():
    lines = None
    with open("input/day11e.txt", "r") as f:
        lines = f.readlines()

    lines = [ l.strip() for l in lines ]

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()