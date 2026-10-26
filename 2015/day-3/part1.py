"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
"""

def open_input_file():
    with open("2015/day-3/input.txt") as f:
        return f.read().strip()

def main():
    instructions = open_input_file()
    # a set is used to store unique houses that receive at least one present
    # if it's a list, it will count duplicates, which we don't want
    houses = set()
    x, y = 0, 0
    houses.add((x, y))

    for char in instructions:
        if char == "^":
            y += 1
        elif char == "v":
            y -= 1
        elif char == ">":
            x += 1
        elif char == "<":
            x -= 1

        houses.add((x, y))

    # print the number of unique houses that received at least one present
    print(len(houses))

if __name__ == "__main__":
    main()