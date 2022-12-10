from typing import List

def part1(lines: List[str]) -> int:
    ans = 0

    tail_visits = set(["0,0"])

    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0

    def adjust_tail():
        nonlocal tail_x, tail_y 

        x_dist = abs(head_x - tail_x)
        y_dist = abs(head_y - tail_y)
        is_touching = x_dist < 2 and y_dist < 2

        if not is_touching:
            if head_x == tail_x:
                # tail approaches head on y
                tail_y = tail_y - 1 if tail_y > head_y else tail_y + 1
            elif head_y == tail_y:
                # tail approaches head on x
                tail_x = tail_x - 1 if tail_x > head_x else tail_x + 1
            else:
                tail_x = tail_x - 1 if tail_x > head_x else tail_x + 1
                tail_y = tail_y - 1 if tail_y > head_y else tail_y + 1
        else:
            pass

        tail_visits.add(f"{tail_x},{tail_y}")

    for line in lines:
        [ dir, distance ] = line.strip().split(" ")
        distance = int(distance)

        for _ in range(0, distance):
            if dir == "D":
                head_y -= 1
            elif dir == "U":
                head_y += 1
            elif dir == "L":
                head_x -= 1
            elif dir == "R":
                head_x += 1

            adjust_tail()
            # print(f"({head_x}, {head_y})")
            # print(f"({tail_x}, {tail_y})")
            # print("----------------------")
            # # input()

    return len(tail_visits)



def part2(lines: List[str]) -> int:
    tail_visits = set(["0,0"])

    head_x, head_y = 0, 0
    knots = [(0,0)] * 9

    def adjust_tail(head, tail):
        head_x, head_y = head
        tail_x, tail_y = tail

        x_dist = abs(head_x - tail_x)
        y_dist = abs(head_y - tail_y)
        is_touching = x_dist < 2 and y_dist < 2

        if not is_touching:
            if head_x == tail_x:
                # tail approaches head on y
                tail_y = tail_y - 1 if tail_y > head_y else tail_y + 1
            elif head_y == tail_y:
                # tail approaches head on x
                tail_x = tail_x - 1 if tail_x > head_x else tail_x + 1
            else:
                tail_x = tail_x - 1 if tail_x > head_x else tail_x + 1
                tail_y = tail_y - 1 if tail_y > head_y else tail_y + 1
        else:
            pass

        return (tail_x, tail_y)


    for line in lines:
        [ dir, distance ] = line.strip().split(" ")
        distance = int(distance)

        for _ in range(0, distance):
            if dir == "D":
                head_y -= 1
            elif dir == "U":
                head_y += 1
            elif dir == "L":
                head_x -= 1
            elif dir == "R":
                head_x += 1

            prev = (head_x, head_y)
            new_knots = []
            for tail in knots:
                new_tail = adjust_tail(prev, tail)
                new_knots.append(new_tail)
                prev = new_tail

            (tail_x, tail_y) = knots[-1]
            tail_visits.add(f"{tail_x},{tail_y}")
            knots = new_knots

    return len(tail_visits)

def main():
    lines = None
    with open("input/day9.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()