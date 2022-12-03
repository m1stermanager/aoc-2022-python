from typing import List

baseline_char = ord('A')

def part1(lines: List[str]) -> int:
    ans = 0

    for line in lines:
        stripped = line.strip()
        line_ln = len(stripped)
        half_ln = int(line_ln/2)
        comp1 = stripped[0:half_ln]
        comp2 = stripped[half_ln:]

        matched_char: str = None
        for char in comp1:
            if char in comp2:
                matched_char = char
                break

        char_ord = ord(matched_char)
        v = 0
        if matched_char.isupper():
            v = char_ord - baseline_char + 27
        else:
            v = char_ord - baseline_char - 27 - 4

        ans += v

    return ans



def part2(lines: List[str]) -> int:
    ans = 0
    buffer = []
    for line in lines:
        stripped = line.strip()
        buffer.append(stripped)

        if len(buffer) == 3:
            matched_char: str = None
            [ elf1, elf2, elf3 ] = buffer
            for char in elf1:
                if char in elf2 and char in elf3:
                    matched_char = char
                    break

            char_ord = ord(matched_char)
            v = 0
            if matched_char.isupper():
                v = char_ord - baseline_char + 27
            else:
                v = char_ord - baseline_char - 27 - 4

            ans += v

            buffer = []

    return ans

def main():
    lines = None
    with open("input/day3.txt", "r") as f:
        lines = f.readlines()

    print("part 1")
    print(part1(lines))
    print("part 2")
    print(part2(lines))

if __name__ == "__main__":
    main()