from collections import defaultdict

def part_1(cards: list[tuple[set[int], set[int]]]) -> int:
    total = 0
    for c in cards:
        total += int(2**(match_count(c) - 1))

    return total

def part_2(cards: list[tuple[set[int], set[int]]]) -> int:
    count = defaultdict(lambda: 0)

    for card_num, card in enumerate(cards):
        count[card_num] += 1
        matches = match_count(card)
        for i in range(card_num + 1, card_num + matches + 1):
            count[i] += count[card_num]

    return sum(count.values())

def match_count(card: tuple[set[int], set[int]]) -> int:
    return len(card[0] & card[1])

def parse_input(inp_file: str) -> list[tuple[set[int], set[int]]]:
    inp = open(inp_file)
    cards = []

    for line in inp.readlines():
        lists = line.split(": ")[1].split(" | ")
        cards.append(tuple(map(lambda l: {int(x) for x in l.split()}, lists)))

    return cards

def main():
    cards = parse_input("input.txt")
    print(part_1(cards))
    print(part_2(cards))

if __name__ == "__main__":
    main()
