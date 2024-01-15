import re
from dataclasses import dataclass

@dataclass
class CubeSet:
    r: int = 0
    g: int = 0
    b: int = 0

    def power(self) -> int:
        return self.r * self.g * self.b

def parse_input(inp_file: str) -> list[list[CubeSet]]:
    inp = open(inp_file)
    games = list()

    pattern = re.compile("[0-9]+ [a-z]")

    for line in inp.readlines():
        sets = [re.findall(pattern, s) for s in line.split(":")[1].split(";")]
        sets = map(lambda selection:
                   {s.split(" ")[1]: int(s.split(" ")[0]) for s in selection},
                   sets)
        games.append([CubeSet(**s) for s in sets])

    return games

def part_1(games: list[list[CubeSet]], possible: CubeSet = CubeSet(r = 12, g = 13, b = 14)) -> int:
    total = 0
    for gid, game in enumerate(games):
        game_id = gid + 1
        is_possible = lambda cs: cs.r <= possible.r and cs.g <= possible.g and cs.b <= possible.b
        total += game_id if all(is_possible(cs) for cs in game) else 0

    return total

def calculate_minimum_set(game: list[CubeSet]) -> CubeSet:
    min_red = 0 
    min_green = 0
    min_blue = 0

    for cs in game:
        min_red = max(cs.r, min_red)
        min_green = max(cs.g, min_green)
        min_blue = max(cs.b, min_blue)

    return CubeSet(min_red, min_green, min_blue)

def part_2(games: list[list[CubeSet]]) -> int:
    return sum(calculate_minimum_set(game).power() for game in games)

def main():
    games = parse_input("input.txt")

    print(part_1(games))
    print(part_2(games))

if __name__ == "__main__":
    main()
