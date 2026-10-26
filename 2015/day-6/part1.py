"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

    turn on 0,0 through 999,999 would turn on (or leave on) every light.
    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?
"""

def open_input_file():
    with open("2015/day-6/input.txt") as f:
        return f.read().splitlines()

def render_instructions(s, grid):
    if "turn on" in s:
        # run turn_on()
        str1 = s.replace("turn on ", "")
        point1 = str1.split(" ")[0]
        point2 = str1.split(" ")[2]
        turn_on(point1, point2, grid)
        pass
    elif "turn off" in s:
        # run turn_off()
        str1 = s.replace("turn off ", "")
        point1 = str1.split(" ")[0]
        point2 = str1.split(" ")[2]
        turn_off(point1, point2, grid)
    else:
        # run toggle()
        str1 = s.replace("toggle ", "")
        point1 = str1.split(" ")[0]
        point2 = str1.split(" ")[2]
        toggle(point1, point2, grid)

def setup_grid():
    # create a 1000x1000 grid of lights, all turned off
    grid = [[False for _ in range(1000)] for _ in range(1000)]
    return grid

def turn_on(point1, point2, grid):
    # turn on all lights in the rectangle defined by point1 and point2
    x1, y1 = map(int, point1.split(","))
    x2, y2 = map(int, point2.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = True

def turn_off(point1, point2, grid):
    # turn off all lights in the rectangle defined by point1 and point2
    x1, y1 = map(int, point1.split(","))
    x2, y2 = map(int, point2.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = False

def toggle(point1, point2, grid):
    # toggle all lights in the rectangle defined by point1 and point2
    x1, y1 = map(int, point1.split(","))
    x2, y2 = map(int, point2.split(","))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            grid[x][y] = not grid[x][y]

def count_lights_on(grid):
    # count the number of lights that are on in the grid
    count = 0
    for row in grid:
        count += sum(row)
    return count

def main():
    instructions = open_input_file()
    grid = setup_grid()
    for row in instructions:
        render_instructions(row, grid)

    print(count_lights_on(grid))

if __name__ == "__main__":
    main()