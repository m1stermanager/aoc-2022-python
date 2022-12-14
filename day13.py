from typing import List
from functools import cmp_to_key
import json

def compare_lists(l, r) -> bool:
    if len(l) == 0 and len(r) != 0:
        return True

    i = 0
    while i < len(l):
        if len(r) < i + 1:
            # right side has fewer items
            return False

        l_val, r_val = l[i], r[i]
        l_is_int = isinstance(l_val, int)
        r_is_int = isinstance(r_val, int)

        if l_is_int and r_is_int:
            if l_val > r_val:
                return False
            if l_val < r_val:
                return True
        elif l_is_int and not r_is_int:
            res = compare_lists([l_val], r_val)
            if res is not None:
                return res
        elif not l_is_int and r_is_int: 
            res= compare_lists(l_val, [r_val])
            if res is not None:
                return res
        elif not l_is_int and not r_is_int:
            res = compare_lists(l_val, r_val)
            if res is not None:
                return res

        i += 1

    if len(l) < len(r):
        return True

    return None

def part1(lines: List[str]) -> int:
    ans = 0

    l_index = 1
    for i in range(0, len(lines), 3):
        # move in chunks of 3 but ditch the newline that is there... 
        [ l, r ] = lines[i:i+3][0:2]
        parsed_l, parsed_r = json.loads(l), json.loads(r)

        in_order = compare_lists(parsed_l, parsed_r)
        if in_order:
            ans += l_index

        l_index += 1


    return ans


def part2(lines: List[str]) -> int:
    ans = 0

    l_index = 1
    parsed_packets = [[[2]], [[6]]]
    for i in range(0, len(lines), 3):
        # move in chunks of 3 but ditch the newline that is there... 
        [ l, r ] = lines[i:i+3][0:2]
        parsed_l, parsed_r = json.loads(l), json.loads(r)
        parsed_packets.extend([parsed_l, parsed_r])

    def sortfunc(l, r):
        res = compare_lists(l, r)
        if res is None:
            return 0
        if res is True:
            return -1
        if res is False:
            return 1

    parsed_packets.sort(key=cmp_to_key(sortfunc))

    div1 = parsed_packets.index([[2]]) + 1
    div2 = parsed_packets.index([[6]]) + 1
    return div1 * div2

def main():
    lines = None
    with open("input/day13.txt", "r") as f:
        lines = f.readlines()

    lines = [ l.strip() for l in lines ]

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()