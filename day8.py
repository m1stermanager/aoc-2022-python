from typing import List

def get_visibility(forest: List[List[int]], direction: str) -> List[List[bool]]:
    output_matrix = [ [ False  for _ in outer ] for outer in forest ]

    # everything is a square
    max_dimension = len(forest) - 1

    r, c = 0, 0
    if direction == "bottom":
        r = max_dimension
    if direction == "right":
        c = max_dimension

    def increment_inner():
        nonlocal c
        nonlocal r
        if direction == "left":
            c += 1
        if direction == "top":
            r += 1
        if direction == "right":
            c -= 1 
        if direction == "bottom":
            r -= 1

    def increment_outer():
        nonlocal c
        nonlocal r
        if direction == "left":
            r += 1
            c = 0
        if direction == "top":
            c += 1
            r = 0
        if direction == "right":
            r += 1
            c = max_dimension
        if direction == "bottom":
            c += 1
            r = max_dimension

    while r < max_dimension + 1 and c < max_dimension + 1 and r >=0 and c >= 0:
        max = -1
        while True:
            if (r > max_dimension or c > max_dimension or r < 0 or c < 0):
                break

            if c == 0 or r == 0 or c == max_dimension or r == max_dimension:
                output_matrix[r][c] = True
                max = forest[r][c]
            else:
                if forest[r][c] > max:
                    output_matrix[r][c] = True
                    max = forest[r][c]
                else:
                    output_matrix[r][c] = False

            increment_inner()

        increment_outer()

    return output_matrix

def part1(lines: List[str]) -> int:
    ans = 0

    forest: List[List[int]] = []

    for line in lines:
        heights = []
        for height in line.strip():
            heights.append(int(height))

        forest.append(heights)

    left_visible = get_visibility(forest, "left")
    # print(left_visible[98])
    top_visible = get_visibility(forest, "top")
    # print(top_visible[98])
    bottom_visible = get_visibility(forest, "bottom")
    # print(bottom_visible[98])
    right_visible = get_visibility(forest, "right")
    # print(len(right_visible[98]))

    y, x = 0, 0
    while y < len(forest):
        x = 0
        while x < len(forest[y]):
            # lets really drive home how out of hand things have gotten
            if left_visible[y][x]:
                ans += 1
            elif right_visible[y][x]:
                ans +=1
            elif top_visible[y][x]:
                ans += 1
            elif bottom_visible[y][x]:
                ans += 1

            x += 1

        y += 1

    return ans



def part2(lines: List[str]) -> int:
    ans = 0

    forest: List[List[int]] = []

    for line in lines:
        heights = []
        for height in line.strip():
            heights.append(int(height))

        forest.append(heights)

    def look_up(y, x) -> int:
        if y == 0:
            return 0

        h = forest[y][x]
        i = 0
        while True:
            i += 1

            offset = (i*-1) + y
            if offset == 0 or forest[offset][x] >= h:
                break

        return i

    def look_down(y, x) -> int:
        if y == (len(forest) - 1):
            return 0

        h = forest[y][x]
        i = 0
        while True:
            i += 1

            offset = i + y
            if offset == len(forest) - 1 or forest[offset][x] >= h:
                break

        return i

    def look_right(y, x) -> int:
        if x == (len(forest[y]) - 1):
            return 0

        h = forest[y][x]
        i = 0
        while True:
            i += 1

            offset = i + x
            if offset == len(forest[y]) -1 or forest[y][offset] >= h:
                break

        return i

    def look_left(y, x) -> int:
        if x == 0:
            return 0

        h = forest[y][x]
        i = 0
        while True:
            i += 1

            offset = (i*-1) + x
            if offset == 0 or forest[y][offset] >= h:
                break

        return i

    y, x = 0, 0
    while y < len(forest):
        x = 0
        while x < len(forest[y]):
            up = look_up(y, x)
            down = look_down(y, x)
            right = look_right(y, x)
            left = look_left(y, x)

            score = up*down*left*right

            if score > ans:
                ans = score

            x += 1

        y += 1

    return ans

def main():
    lines = None
    with open("input/day8.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()