from typing import List

def get_neighbors(coord, unvisited_set):
    (y, x) = coord

    res = [ 
        (y+1, x), # up
        (y-1, x), # down
        (y, x-1), # left
        (y, x+1)  # right
    ]

    return [ x for x in res if x in unvisited_set ]

def print_values(values):
    for line in values:
        printable = [ str(v).zfill(5) if v is not None else "-----" for v in line ]
        for p in printable:
            print(p, end="|")

        print()

def part1(lines: List[str]) -> int:
    ans = 0

    heights = []
    values = []
    value_map = {}
    start = ()
    current = ()
    dest = ()
    unvisited = set()

    for y, line in enumerate(lines):
        line_heights = []
        line_values = []
        for x, char in enumerate(line):
            if char == "S":
                line_values.append(0)
                line_heights.append(ord('a'))
                start = (y, x)
                value_map[start] = 0
            elif char == "E":
                line_values.append(None)
                line_heights.append(ord('z'))
                dest = (y, x)
                value_map[dest] = None
            else:
                line_values.append(None)
                line_heights.append(ord(char))
                value_map[(y, x)] = None

            unvisited.add((y, x))

        heights.append(line_heights)
        values.append(line_values)

    current = (start[0], start[1])
    # no idea if this is a good idea
    visit_stack = []
    # while len(unvisited) > 0:
    while dest in unvisited:
        (cur_y, cur_x) = current
        cur_height = heights[cur_y][cur_x]
        cur_val = values[cur_y][cur_x]

        eligible_neighbors = get_neighbors(current, unvisited)
        neighbor_distances = []

        for neighbor in eligible_neighbors:
            (n_y, n_x) = neighbor
            n_val = values[n_y][n_x]
            can_travel = (heights[n_y][n_x] - cur_height) <= 1
            if not can_travel:
                continue

            dist = cur_val + 1
            if n_val is None or dist < n_val:
                values[n_y][n_x] = dist
            neighbor_distances.append((neighbor, dist))

        neighbor_distances.sort(key=lambda d: d[1], reverse=True)
        for nd in neighbor_distances:
            visit_stack.append(nd[0])
            value_map[nd[0]] = nd[1]

        unvisited.remove(current)

        # inefficient
        lowest = ()
        lowest_val = 999999
        for k, v in value_map.items():
            if not v:
                continue
            if k not in unvisited:
                continue

            if v < lowest_val:
                lowest = k
                lowest_val = v

        if lowest == ():
            break

        current = lowest

    # print_values(values)
    return values[dest[0]][dest[1]]


def part2(lines: List[str]) -> int:
    ans = 999999999

    heights = []
    dest = ()

    root_unvisited = set()
    root_value_map = dict()
    starting_points = []

    for y, line in enumerate(lines):
        line_heights = []
        line_values = []
        for x, char in enumerate(line):
            if char == "S" or char == "a":
                # line_values.append(0)
                line_values.append(None)
                line_heights.append(ord('a'))
                # start = (y, x)
                root_value_map[(y, x)] = None
                starting_points.append((y, x))
            elif char == "E":
                line_values.append(None)
                line_heights.append(ord('z'))
                dest = (y, x)
                root_value_map[dest] = None
            else:
                line_values.append(None)
                line_heights.append(ord(char))
                root_value_map[(y, x)] = None

            root_unvisited.add((y, x))

        heights.append(line_heights)
        # values.append(line_values)

    final_maps = []
    for sp in starting_points:
        # values = []
        value_map = root_value_map.copy()
        # start = ()
        current = ()
        unvisited = root_unvisited.copy()

        current = (sp[0], sp[1])
        # values[sp[0]][sp[1]] = 0
        value_map[current] = 0

        # while len(unvisited) > 0:
        while dest in unvisited:
            (cur_y, cur_x) = current
            cur_height = heights[cur_y][cur_x]
            cur_val = value_map[current]

            eligible_neighbors = get_neighbors(current, unvisited)
            # neighbor_distances = []

            for neighbor in eligible_neighbors:
                (n_y, n_x) = neighbor
                n_val = value_map[neighbor]
                can_travel = (heights[n_y][n_x] - cur_height) <= 1
                if not can_travel:
                    continue

                dist = cur_val + 1
                if n_val is None or dist < n_val:
                    # values[n_y][n_x] = dist
                    value_map[neighbor] = dist

                # value_map[neighbor] = dist
                # neighbor_distances.append((neighbor, dist))

            # neighbor_distances.sort(key=lambda d: d[1], reverse=True)
            # for nd in neighbor_distances:
            #     value_map[nd[0]] = nd[1]

            unvisited.remove(current)

            # inefficient
            lowest = ()
            lowest_val = 999999
            for k, v in value_map.items():
                if not v:
                    continue
                if k not in unvisited:
                    continue

                if v < lowest_val:
                    lowest = k
                    lowest_val = v

            if lowest == ():
                # t = value_map[(dest[0], dest[1])]
                # if t and ans > t:
                #     ans = t
                break

            current = lowest
        final_maps.append(value_map)

    for m in final_maps:
        if m[dest] and m[dest] < ans:
            ans = m[dest]
    # print_values(values)
    return ans

def main():
    lines = None
    with open("input/day12.txt", "r") as f:
        lines = f.readlines()

    lines = [ l.strip() for l in lines ]

    # lines = [
    #     "Sabqponm",
    #     "abcryxxl",
    #     "accszExk",
    #     "acctuvwj",
    #     "abdefghi"
    # ]

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()