#!/usr/bin/env python3

input_file = "input"


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

    number_sets = set()

    for i, array in enumerate(matrix):
        for j, char in enumerate(array):
            if char.isdigit() or char == ".":
                continue
            adjacent_digits_set = find_adjacent_digits(matrix, i, j)
            number_sets.update(adjacent_digits_set)
    print(number_sets)

    numbers_array = []

    for r, c in number_sets:
        s = ""
        while c < len(matrix[r]) and matrix[r][c].isdigit():
            s += matrix[r][c]
            c += 1

        numbers_array.append(int(s))
    print(numbers_array)
    print(sum(numbers_array))
