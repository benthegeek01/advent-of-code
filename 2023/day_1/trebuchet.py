DIGITS = ["zero", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine"]
R_DIGITS = ["".join(list(reversed(s)))for s in DIGITS]

def part_1() -> int:
    inp = open("input.txt")

    total = 0

    for line in inp.readlines():
        digits = filter(lambda c: c if c.isdigit() else "", line)
        num = "".join(digits)
        total += int(num[0] + num[-1])

    return total

def part_2() -> int:
    inp = open("input.txt")
    total = 0

    for line in inp.readlines():
        # Calculate array of (digit, str_digit_index) and filter out digits not
        # in line
        first_s_pos = list(filter(lambda t: t[1] != - 1,
                                  enumerate([line.find(s) for s in DIGITS])))
        # Find first string digit position (if one exists, otherwise discard
        # variable)
        first_s_pos = sorted(first_s_pos,
                             key = lambda t: t[1])[0] if len(first_s_pos) > 0\
                                                      else (-1, float('inf'))

        # Same but for reversed line/string_digits
        last_s_pos = ["".join(list(reversed(line))).find(s) for s in R_DIGITS]
        # Some maths that takes reversed line index and converts to normal
        # index using length of string_digit and line
        last_s_pos =    list(
                        filter(lambda t: t[1] != -1,
                            enumerate(
                            list(
                            map(lambda t: len(line) - 1 - t[0] - (len(t[1]) - 1)
                                if t[0] != -1 else -1, zip(last_s_pos, R_DIGITS\
                        ))))))
        last_s_pos = sorted(last_s_pos,
                            key = lambda t: -t[1])[0] if len(last_s_pos) > 0\
                                                        else (-1, -float('inf'))


        # Find first and last digit in line
        first_digit_i = find_first_digit(line)
        last_digit_i = len(line) - 1 - find_first_digit("".join(list(reversed(line))))

        # Choose whichever minimum/maximum index is to use for digit for
        # first/last
        first_digit = line[first_digit_i] if first_digit_i < first_s_pos[1]\
                                            else str(first_s_pos[0])
        last_digit = line[last_digit_i] if last_digit_i > last_s_pos[1]\
                                        else str(last_s_pos[0])


        total += int(first_digit + last_digit)

    return total

def find_first_digit(s: str) -> int:
    for c in range(len(s)):
        if s[c].isdigit():
            return c

    return -1

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()
