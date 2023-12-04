#!/usr/bin/env python3

input_file = "input"
file = open(input_file).read().splitlines()

cards = [cards.split(": ")[1] for cards in file]

total_points = 0

for card in cards:
    winning_cards, my_cards = card.strip().split(" | ")
    winning_cards = [s for s in winning_cards.split(" ") if s]
    my_cards = [s for s in my_cards.split(" ") if s]
    my_wins = set(winning_cards).intersection(set(my_cards))
    if my_wins:
        total_points += pow(2, len(my_wins) - 1)

print(total_points)
