#!/usr/bin/env python3

input_file = "input"
sum = 0

with open(input_file, "r") as file:
    for line in file:
        line = (
            line.replace("nine", "n9ine")
            .replace("eight", "e8ight")
            .replace("seven", "s7even")
            .replace("six", "s6ix")
            .replace("five", "f5ive")
            .replace("four", "f4our")
            .replace("three", "t3hree")
            .replace("two", "t2wo")
            .replace("one", "o1ne")
        )
        my_array = [(s) for s in line.strip() if s.isdigit()]
        sum += int(str(my_array[0]) + str(my_array[-1]))

print(sum)
