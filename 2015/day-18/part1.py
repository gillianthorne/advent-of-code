"""
--- Day 18: Like a GIF For Your Yard ---

After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. You arrange them in a 100x100 grid.

Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. With so few lights, he says, you'll have to resort to animation.

Start by setting your lights to the included initial configuration (your puzzle input). A # means "on", and a . means "off".

Then, animate your grid in steps, where each step decides the next configuration based on the current one. Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, which is on an edge, only has the neighbors marked 1 through 5:

1B5...
234...
......
..123.
..8A4.
..765.

The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

    A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
    A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.

All of the lights update simultaneously; they all consider the same current state before moving to the next.

Here's a few steps from an example configuration of another 6x6 grid:

Initial state:
.#.#.#
...##.
#....#
..#...
#.#..#
####..

After 1 step:
..##..
..##.#
...##.
......
#.....
#.##..

After 2 steps:
..###.
......
..###.
......
.#....
.#....

After 3 steps:
...#..
......
...#..
..##..
......
......

After 4 steps:
......
......
..##..
..##..
......
......

After 4 steps, this example has four lights on.

In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?
"""

def open_input_file():
    with open("2015/day-18/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def get_grid(lines):
    grid = []
    for line in lines:
        row = []
        # turn it into a list of 1s and 0s, where 1 is on and 0 is off
        for char in line:
            if char == "#":
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid

def count_neighbors(grid, x, y):
    # count the number of neighbors that are on
    count = 0
    # loop through the 8 neighbors
    for i in range(-1, 2):
        for j in range(-1, 2):
            # skip the center cell
            if i == 0 and j == 0:
                continue
            # check if the neighbor is in bounds
            # if x + i (so the cells on the direct left or right) or y + j (so the cells directly above or below) is greater than or equal to 0 and less than the length of the grid, then it is in bounds
            # because i used 0, 1 for on/off, i can just add the value of the neighbor to the count, because if it is on, it will add 1, and if it is off, it will add 0
            # i and j can be negative, so x + i will still basically be x - i in the first step, and y + j will still basically be y - j in the first step, so it will still check the cells directly above and to the left of the current cell
            # to count the diagonal neighbors, it is when i and j are both not 0, so it will check the cells diagonally above and to the left, diagonally above and to the right, diagonally below and to the left, and diagonally below and to the right - if one is zero and the other is not, it will check the cells directly above, below, left, and right
            if x + i >= 0 and x + i < len(grid) and y + j >= 0 and y + j < len(grid[0]):
                count += grid[x + i][y + j]
    return count

def step(grid):
    # create a new grid to hold the next state
    new_grid = []
    # loop through the grid
    for i in range(len(grid)):
        new_row = []
        for j in range(len(grid[0])):
            # count the number of neighbors that are on
            neighbors = count_neighbors(grid, i, j)
            # apply the rules
            if grid[i][j] == 1:
                if neighbors == 2 or neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
            else:
                if neighbors == 3:
                    new_row.append(1)
                else:
                    new_row.append(0)
        new_grid.append(new_row)

    return new_grid

def main():
    lines = open_input_file()
    grid = get_grid(lines)
    for i in range(100):
        grid = step(grid)
    # count the number of lights that are on
    count = 0
    for row in grid:
        count += sum(row)
    print(count)

if __name__ == "__main__":
    main()