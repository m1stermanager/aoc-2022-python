from typing import List


their_rock = "A"
their_paper = "B"
their_scissors = "C"

my_rock = "X"
my_paper = "Y"
my_scissors = "Z"

def part1(lines: List[str]) -> int:
    score = 0
    for line in lines:
        them = line[0]
        me = line[2]

        if me == my_rock:
            score += 1
            if them == their_rock:
                score += 3
            if them == their_scissors:
                score += 6

        if me == my_paper:
            score += 2
            if them == their_paper:
                score += 3
            if them == their_rock:
                score += 6
        if me == my_scissors:
            score += 3
            if them == their_scissors:
                score += 3
            if them == their_paper:
                score += 6

    return score

def part2(lines: List[str]) -> int:
    score = 0
    for line in lines:
        them = line[0]
        me = line[2]

        # not going to adjust these variable names right now
        if me == my_rock:
            # i need to lose
            if them == their_rock:
                score += 3
            elif them == their_scissors:
                score += 2
            else:
                score += 1

        if me == my_paper:
            score += 3
            if them == their_rock:
                score +=  1
            if them == their_paper:
                score += 2
            if them == their_scissors:
                score += 3

        if me == my_scissors:
            score += 6
            if them == their_rock:
                score +=  2
            if them == their_paper:
                score += 3
            if them == their_scissors:
                score += 1

    return score

def main():
    lines = None
    with open("input/day2.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()