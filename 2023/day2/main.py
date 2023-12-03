#!/usr/bin/env python3

input_file = "./input"

# 12 red cubes, 13 green cubes, and 14 blue cubes
with open(input_file, "r") as file:
    total_sum = 0
    total_power = 0
    for game_no, game in enumerate(file):
        b, g, r = 0, 0, 0
        possible = True
        print(f"=== GAME NUMBER: {game_no+1} ===")
        print(game.strip())
        for cube in game.strip().split(": ")[1].replace(";", ",").split(", "):
            quantity, color = cube.split(" ")
            quantity = int(quantity)
            if color == "blue":
                if quantity > b:
                    b = quantity
                if quantity > 14:
                    possible = False
            elif color == "green":
                if quantity > g:
                    g = quantity
                if quantity > 13:
                    possible = False
            elif color == "red":
                if quantity > r:
                    r = quantity
                if quantity > 12:
                    possible = False

        print(f"+ Minimum Numbers")
        print(f"| Blue: {b}")
        print(f"| Green: {g}")
        print(f"| Red: {r}")
        total_power += b * g * r

        if possible:
            print(f"Game {game_no+1} is possible")
            total_sum += game_no + 1
        else:
            print(f"Game {game_no+1} is NOT possible")
            pass

        print()
    print(f"Part1: {total_sum}")
    print(f"Part2: {total_power}")
