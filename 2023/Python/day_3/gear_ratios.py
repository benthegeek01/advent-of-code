def parse_input(inp_file: str):
    inp = open(inp_file)
    grid = []

    for line in inp.readlines():
        grid.append(line.replace("\n", ""))

    return grid

def is_valid_pos(grid: list[str], x: int, y: int) -> bool:
    if x < 0 or x >= len(grid[0]):
        return False
    if y < 0 or y >= len(grid):
        return False

    return True

def char_at_pos(grid: list[str], x: int, y: int) -> str:
    if not is_valid_pos(grid, x, y):
        return ""
    
    return grid[y][x]

def adjacent_positions(x: int, y: int) -> set:
    positions = set()
    for x_diff in range(-1, 2):
        for y_diff in range(-1, 2):
            if x_diff == 0 and y_diff == 0:
                continue
            positions.add((x + x_diff, y + y_diff))

    return positions


def adjacent_positions_for_length(x: int, y: int, l: int):
    positions = set()
    for x_c in range(x, x + l):
        adjacent = adjacent_positions(x_c, y)
        adjacent = set(filter(lambda t: t[1] != y, adjacent))

        positions = positions | adjacent

    positions.add((x - 1, y))
    positions.add((x + l, y))

    return positions

def find_length_of_num(grid: list[str], x: int, y: int) -> int:
    curr_x = x + 1
    l = 1
    while char_at_pos(grid, curr_x, y).isdigit():
        l += 1
        curr_x += 1

    return l


def part_1(grid: list[str]) -> int:
    total = 0
    for y in range(len(grid)):
        curr_x = 0
        while curr_x < len(grid[0]):
            if not char_at_pos(grid, curr_x, y).isdigit():
                curr_x += 1
            else:
                l = find_length_of_num(grid, curr_x, y)

                for pos in adjacent_positions_for_length(curr_x, y, l):
                    ch = char_at_pos(grid, pos[0], pos[1])
                    if ch != "" and ch != "." and not ch.isdigit():
                        total += int(grid[y][curr_x:curr_x + l])
                        break

                curr_x += l

    return total

def get_x_of_num_start(grid: list[str], x: int, y: int) -> int:
    curr_x = x - 1
    while char_at_pos(grid, curr_x, y).isdigit():
        curr_x -= 1

    return curr_x + 1

def part_2(grid: list[str]):
    total = 0
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if char_at_pos(grid, x, y) == "*":
                adjacent = adjacent_positions(x, y)
                dig_adj = list(filter(lambda t: char_at_pos(grid, t[0], t[1]).isdigit(), adjacent))
                distinct_nums = list({(get_x_of_num_start(grid, pos[0], pos[1]), pos[1]) for pos in dig_adj})

                if len(distinct_nums) == 2:
                    prod = 1
                    for pos in distinct_nums:
                        l = find_length_of_num(grid, pos[0], pos[1])
                        prod *= int(grid[pos[1]][pos[0]:pos[0] + l])

                    total += prod

    return total

def main():
    grid = parse_input("input.txt")
    print(part_1(grid))
    print(part_2(grid))

if __name__ == "__main__":
    main()
