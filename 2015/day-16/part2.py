"""
--- Day 16: Aunt Sue ---

Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

    children, by human DNA age analysis.
    cats. It doesn't differentiate individual breeds.
    Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
    goldfish. No other kinds of fish.
    trees, all in one group.
    cars, presumably by exhaust or gasoline or something.
    perfumes, which is handy, since many of your Aunts Sue wear a few kinds.

In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1

You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?

--- Part Two ---

As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

What is the number of the real Aunt Sue?
"""

def open_input_file():
    with open("2015/day-16/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def get_sue(lines):
    sues = {}
    for sue in lines:
        split = sue.split()
        number = split[1][:-1] # ignore the colon
        item1 = split[2][:-1]
        count1 = split[3][:-1]
        item2 = split[4][:-1]
        count2 = split[5][:-1]
        item3 = split[6][:-1]
        count3 = split[7] # no extra punctuation at the end of this one
        sues[number] = {
            item1: count1,
            item2: count2,
            item3: count3
        }
    return sues

def match_sues(match, sues):
    for number, items in sues.items():
        # check if all items in the current sue match the items in the match dictionary
        # we need to check for the special cases of cats, trees, pomeranians, and goldfish
        # this is really messy but basically if the item is in the match, then (if it's cats or trees, the count needs to be greater than the match count), or if it's (pomeranians or goldfish, the count needs to be less than the match count), otherwise it needs to be equal to the match count
        if all(
            (item in match and (
                (item == "cats" or item == "trees") and int(match[item]) < int(count) or
                (item == "pomeranians" or item == "goldfish") and int(match[item]) > int(count) or
                (item != "cats" and item != "trees" and item != "pomeranians" and item != "goldfish") and match[item] == count
            )) for item, count in items.items()
        ):
            return number
        # if all(item in match and match[item] == count for item, count in items.items()):
        #     return number
    return None

def main():
    lines = open_input_file()
    sues = get_sue(lines)
    match = {
        "children": "3",
        "cats": "7",
        "samoyeds": "2",
        "pomeranians": "3",
        "akitas": "0",
        "vizslas": "0",
        "goldfish": "5",
        "trees": "3",
        "cars": "2",
        "perfumes": "1"
    }
    matching_sue = match_sues(match, sues)
    print(matching_sue)

if __name__ == "__main__":
    main()