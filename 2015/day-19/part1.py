"""
--- Day 19: Medicine for Rudolph ---

Rudolph the Red-Nosed Reindeer is sick! His nose isn't shining very brightly, and he needs medicine.

Red-Nosed Reindeer biology isn't similar to regular reindeer biology; Rudolph is going to need custom-made medicine. Unfortunately, Red-Nosed Reindeer chemistry isn't similar to regular reindeer chemistry, either.

The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH

Given the replacements above and starting with HOH, the following molecules could be generated:

    HOOH (via H => HO on the first H).
    HOHO (via H => HO on the second H).
    OHOH (via H => OH on the first H).
    HOOH (via H => OH on the second H).
    HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?
"""

def open_input_file():
    # this one has two parts, the first part is the replacements, the second part is the medicine molecule. we can split the input on the empty line to get the two parts.
    with open("2015/day-19/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    # find the index of the empty line
    empty_line_index = lines.index("")
    # the replacements are the lines before the empty line, and the medicine molecule is the line after the empty line
    replacements = lines[:empty_line_index]
    medicine_molecule = lines[empty_line_index + 1]
    return replacements, medicine_molecule

def get_replacements(lines):
    replacements = {}
    for line in lines:
        # split the line on the " => " to get the from and to parts
        from_part, to_part = line.split(" => ")
        # there are multiple replacements for the same from part, so we need to store them in a list
        # if the from part is not in the dictionary, we need to create a new list for it
        if from_part not in replacements:
            replacements[from_part] = []
        # add the to part to the list of replacements for the from part, either if it was just created or if it already existed
        replacements[from_part].append(to_part)

    return replacements

def get_distinct_molecules(replacements, medicine_molecule):
    distinct_molecules = set()
    # loop through the replacements, and for each replacement, loop through the medicine molecule to find all occurrences of the from part. for each occurrence, create a new molecule by replacing the from part with the to part, and add it to the set of distinct molecules.
    for from_part, to_parts in replacements.items():
        # find all occurrences of the from part in the medicine molecule
        start_index = 0
        while True:
            # find the index of the next occurrence of the from part
            index = medicine_molecule.find(from_part, start_index)
            # if there are no more occurrences, break out of the loop
            if index == -1:
                break
            # for each to part, create a new molecule by replacing the from part with the to part, and add it to the set of distinct molecules
            for to_part in to_parts:
                new_molecule = medicine_molecule[:index] + to_part + medicine_molecule[index + len(from_part):]
                distinct_molecules.add(new_molecule)
            # update the start index to be after the current occurrence of the from part
            start_index = index + 1

    return distinct_molecules

def main():
    replacements_lines, medicine_molecule = open_input_file()
    replacements = get_replacements(replacements_lines)
    distinct_molecules = get_distinct_molecules(replacements, medicine_molecule)
    # get the length of the set of distinct molecules, which is the number of distinct molecules that can be created after all the different ways you can do one replacement on the medicine molecule
    print(len(distinct_molecules))

if __name__ == "__main__":
    main()