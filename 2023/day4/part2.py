#!/usr/bin/env python3

input_file = "test"
file = open(input_file).read().splitlines()

m = {}

cards = [cards.split(": ")[1] for cards in file]
print(f"=== Total Cards {len(cards)} ===\n")

for card_no, card in enumerate(cards):
    if card_no not in m:
        m[card_no] = 1  # We already have one copy of all the scratch cards
    winning_cards, my_cards = card.strip().split(" | ")
    winning_cards = [s for s in winning_cards.split(" ") if s]
    my_cards = [s for s in my_cards.split(" ") if s]
    my_matches = set(winning_cards).intersection(set(my_cards))
    print(f"=== Card No. {card_no} ===")
    print(f"+ Matches in Card No. {card_no}: {len(my_matches)}")
    for nc in range(card_no + 1, len(my_matches) + card_no + 1):
        print(f"++ Processing Card No. {nc}, adding {m.get(nc, 1)} + {m[card_no]}")
        m[nc] = m.get(nc, 1) + m[card_no]
        print(f"+++ {m}")
    print()

print(f"=== Final Map ===")
print(m)
print(sum(m.values()))
