from typing import List

def part1(lines: List[str]) -> int:
    ans = 0
    dir = dict()

    current_dir = ""
    for line in lines:
        if line.startswith("$ cd"):
            new_dir = line.replace("$ cd", "").strip()
            if new_dir == "/":
                current_dir = "/"
            elif new_dir == "..":
                current_dir = "/".join(current_dir.split("/")[0:-1])
            else:
                current_dir = current_dir.rstrip("/") + "/" + new_dir

            if current_dir not in dir:
                dir[current_dir] = 0

        elif line.startswith("$ ls"):
            # ls, maybe we need to do something?
            pass
        elif line.startswith("dir"):
            # we're in a particular subdirectory, but I don't think I care right now
            pass
        else:
            affected_directories = current_dir.split("/")

            [ size, filename ] = line.split(" ")
            tmp = "/"
            for affected in affected_directories:
                tmp = tmp.rstrip("/") + "/" + affected
                dir[tmp] += int(size)


    large_directories = [ s for s in dir.values() if s <= 100000 ]
    return sum(large_directories)



def part2(lines: List[str]) -> int:
    ans = 0
    line = lines[0]

    dir = dict()

    current_dir = ""
    for line in lines:
        prev = current_dir
        if line.startswith("$ cd"):
            new_dir = line.replace("$ cd", "").strip()
            if new_dir == "/":
                current_dir = "/"
            elif new_dir == "..":
                current_dir = "/".join(current_dir.split("/")[0:-1])
                if current_dir == "":
                    current_dir = "/"
            else:
                current_dir = current_dir.rstrip("/") + "/" + new_dir

            if current_dir not in dir:
                dir[current_dir] = 0

        elif line.startswith("$ ls"):
            # ls, maybe we need to do something?
            pass
        elif line.startswith("dir"):
            # we're in a particular subdirectory, but I don't think I care right now
            pass
        else:
            [ size, filename ] = line.split(" ")

            tmp = "/"
            affected_directories = []

            if current_dir == "/":
                dir["/"] += int(size)
            else:
                affected_directories = current_dir.split("/")
                for affected in affected_directories:
                    tmp = tmp.rstrip("/") + "/" + affected
                    dir[tmp] += int(size)


    free_space = 70000000 - dir["/"]
    needed_space = 30000000 - free_space
    # lets find the smallest number that is >= needed_space

    # just pump up ans to initialize a large value
    ans = dir["/"]
    for s in dir.values():
        if s >= needed_space and s < ans:
            ans = s

    return ans

def main():
    lines = None
    with open("input/day7.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()