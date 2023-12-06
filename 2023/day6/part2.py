#!/usr/bin/env pypy3

file_input = "input"

time, distance = open(file_input).read().strip().split("\n")

time = [int(x) for x in time.split() if x.isdigit()]
time = int("".join(map(str, time)))

distance = [int(x) for x in distance.split() if x.isdigit()]
distance = int("".join(map(str, distance)))

ways_to_win = []

print(f"=== Race: {distance}/{time} mm/ms ===")
count = 0
for btn_press in range(0, time):
    speed = btn_press
    dist = (time - btn_press) * speed
    if dist > distance:
        count += 1
ways_to_win.append(count)

product = 1
for w2w in ways_to_win:
    product *= w2w

print(ways_to_win)
print(product)
