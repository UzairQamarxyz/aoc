#!/usr/bin/env python3

input_file = "input"

total_power = 0


def find_adjacent_digits(matrix, r, c):
    c_set = set()
    for cr in (r - 1, r, r + 1):
        for cc in (c - 1, c, c + 1):
            if (
                0 >= cc > len(matrix)
                or 0 >= cc > len(matrix[0])
                and not matrix[cr][cc].isdigit()
            ):
                continue
            if matrix[cr][cc].isdigit():
                while cc > 0 and matrix[cr][cc - 1].isdigit():
                    cc -= 1
                c_set.add((cr, cc))
    return c_set


with open(input_file, "r") as file:
    matrix = [[y.strip() for y in x.strip()] for x in file]

    for i, array in enumerate(matrix):
        for j, char in enumerate(array):
            if char != "*":
                continue

            number_sets = set()

            adjacent_digits_set = find_adjacent_digits(matrix, i, j)
            if len(adjacent_digits_set) > 1:
                number_sets.update(adjacent_digits_set)
            else:
                continue
            print(number_sets)

            numbers_array = []

            for r, c in number_sets:
                s = ""
                while c < len(matrix[r]) and matrix[r][c].isdigit():
                    s += matrix[r][c]
                    c += 1

                numbers_array.append(int(s))
            total_power += numbers_array[0] * numbers_array[1]
            print(numbers_array)

print(total_power)
