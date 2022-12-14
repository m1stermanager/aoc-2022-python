from typing import List

def print_cavern(min_x, max_x, min_y, max_y, formations: set, settled_sand = set(), sand=()):
    max_x = max(max_x, 500)
    min_x = min(min_x, 500)

    for y in range(0, max_y+1):
        print(f"{str(y).zfill(4)} ", end="")
        for x in range(min_x, max_x + 1):
            p = (x, y)
            if p == sand:
                print("@", end="")
            elif p == (500, 0):
                print("+", end="")
            elif p in settled_sand:
                print("o", end="")
            elif p in formations:
                print("#", end="")
            else:
                print(".", end="")

        print()

def part1(lines: List[str]) -> int:
    ans = 0

    min_x = 999999
    max_x = -99999

    min_y = 0 
    max_y = -99999

    rock_formations = set()
    for line in lines:
        points = line.split(" -> ")
        for i in range(0, len(points)):
            seg = points[i:i+2]
            if len(seg) < 2:
                break

            [ start, end ] = seg 
            [ start_x, start_y ] = map(int, start.split(","))
            [ end_x, end_y ] = map(int, end.split(","))
            
            min_x = min(start_x, end_x, min_x)
            max_x = max(start_x, end_x, max_x)
            min_y = min(start_y, end_y, min_y)
            max_y = max(start_y, end_y, max_y)

            if start_x != end_x:
                dir = 1 if start_x < end_x else -1
                for i in range(0, abs(start_x-end_x)+1):
                    rock_formations.add((start_x+(i*dir), start_y))

            if start_y != end_y:
                dir = 1 if start_y < end_y else -1
                for i in range(0, abs(start_y-end_y)+1):
                    rock_formations.add((start_x, start_y+(i*dir)))


    settled_sand = set()
    # print_cavern(min_x, max_x, min_y, max_y, rock_formations)
    while True:
        sand = (500, 0)
        while True:
            s_x, s_y = sand
            locations = [ 
                (s_x, s_y+1),
                (s_x-1, s_y+1),
                (s_x+1, s_y+1)
            ]

            new_location = list(filter(lambda x: x not in rock_formations and x not in settled_sand, locations))[0:1]
            if new_location == []:
                settled_sand.add(sand)
                break

            new_x, new_y = new_location[0]
            if new_y > max_y:
                # its over beast no more sand
                print_cavern(min_x, max_x, min_y, max_y, rock_formations, settled_sand, sand)
                return len(settled_sand)
            else:
                sand = (new_x, new_y)

            # print_cavern(min_x, max_x, min_y, max_y, rock_formations, settled_sand, sand)
            # input()

    return ans


def part2(lines: List[str]) -> int:
    ans = 0

    min_x = 999999
    max_x = -99999

    min_y = 0 
    max_y = -99999

    rock_formations = set()
    for line in lines:
        points = line.split(" -> ")
        for i in range(0, len(points)):
            seg = points[i:i+2]
            if len(seg) < 2:
                break

            [ start, end ] = seg 
            [ start_x, start_y ] = map(int, start.split(","))
            [ end_x, end_y ] = map(int, end.split(","))
            
            min_x = min(start_x, end_x, min_x)
            max_x = max(start_x, end_x, max_x)
            min_y = min(start_y, end_y, min_y)
            max_y = max(start_y, end_y, max_y)

            if start_x != end_x:
                dir = 1 if start_x < end_x else -1
                for i in range(0, abs(start_x-end_x)+1):
                    rock_formations.add((start_x+(i*dir), start_y))

            if start_y != end_y:
                dir = 1 if start_y < end_y else -1
                for i in range(0, abs(start_y-end_y)+1):
                    rock_formations.add((start_x, start_y+(i*dir)))


    max_y = max_y + 2
    settled_sand = set()
    # print_cavern(min_x, max_x, min_y, max_y, rock_formations)
    while True:
        sand = (500, 0)
        while True:
            s_x, s_y = sand
            locations = [ 
                (s_x, s_y+1),
                (s_x-1, s_y+1),
                (s_x+1, s_y+1)
            ]

            new_location = list(filter(lambda x: x not in rock_formations and x not in settled_sand, locations))[0:1]
            if new_location == []:
                if sand == (500, 0):
                    print_cavern(min_x, max_x, min_y, max_y, rock_formations, settled_sand, sand)
                    return len(settled_sand) + 1
                else:
                    settled_sand.add(sand)
                    break

            new_x, new_y = new_location[0]
            min_x = min(min_x, new_x)
            max_x = max(max_x, new_x)

            if new_y == (max_y - 1):
                # its over beast no more sand
                # print_cavern(min_x, max_x, min_y, max_y, rock_formations, settled_sand, sand)
                settled_sand.add((new_x, new_y))
            else:
                sand = (new_x, new_y)

def main():
    lines = None
    with open("input/day14.txt", "r") as f:
        lines = f.readlines()

    lines = [ l.strip() for l in lines ]

    # lines = [
    #     "498,4 -> 498,6 -> 496,6",
    #     "503,4 -> 502,4 -> 502,9 -> 494,9"
    # ]

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()