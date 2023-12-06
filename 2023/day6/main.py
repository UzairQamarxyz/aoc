#!/usr/bin/env pypy3

file_input = "input"

time, distance = open(file_input).read().strip().split("\n")
time = [int(x) for x in time.split(":")[1].strip().split(" ") if x]
distance = [int(x) for x in distance.split(":")[1].strip().split(" ") if x]

ways_to_win = []

for i in range(0, len(time)):
    print(f"=== Race No. {i}: {distance[i]}/{time[i]} mm/ms ===")
    count = 0
    for btn_press in range(0, time[i]):
        speed = btn_press
        dist = (time[i] - btn_press) * speed
        if dist > distance[i]:
            print(f"+ Covered {dist} with {btn_press}ms button press")
            count += 1
    ways_to_win.append(count)

product = 1
for w2w in ways_to_win:
    product *= w2w

print(ways_to_win)
print(product)
