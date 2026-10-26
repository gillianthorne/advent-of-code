"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

    > delivers presents to 2 houses: one at the starting location, and one to the east.
    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""

def open_input_file():
    with open("2015/day-3/input.txt") as f:
        return f.read().strip()

def main():
    instructions = open_input_file()
    # a set is used to store unique houses that receive at least one present
    # if it's a list, it will count duplicates, which we don't want
    houses = set()
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0

    # adding robo_santa here is a little redundant because it starts at the same location as santa, but it makes the code more readable
    houses.add((santa_x, santa_y))
    houses.add((robo_x, robo_y))

    for i, char in enumerate(instructions):
        if i % 2 == 0:  # Santa's turn
            if char == "^":
                santa_y += 1
            elif char == "v":
                santa_y -= 1
            elif char == ">":
                santa_x += 1
            elif char == "<":
                santa_x -= 1

            houses.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if char == "^":
                robo_y += 1
            elif char == "v":
                robo_y -= 1
            elif char == ">":
                robo_x += 1
            elif char == "<":
                robo_x -= 1

            houses.add((robo_x, robo_y))

    # print the number of unique houses that received at least one present
    print(len(houses))

if __name__ == "__main__":
    main()