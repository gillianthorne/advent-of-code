"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?
"""
from itertools import permutations

def open_input_file():
    with open("2015/day-13/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def compute_happiness(lines):
    happiness = {}
    for line in lines:
        parts = line.split()
        person1 = parts[0]
        person2 = parts[-1][:-1]  # remove the trailing period
        change = int(parts[3])
        if parts[2] == "lose":
            change = -change
        # store the happiness change in a dictionary with a tuple of (person1, person2) as the key
        happiness[(person1, person2)] = change

    return happiness

def optimal_seating(happiness):
    people = set()
    # gather all unique people from the happiness dictionary
    for person1, person2 in happiness.keys():
        people.add(person1)
        people.add(person2)

    # generate all permutations of the people to find the optimal seating arrangement
    max_happiness = float('-inf')
    for perm in permutations(people):
        total_happiness = 0
        for i in range(len(perm)):
            person1 = perm[i]
            person2 = perm[(i + 1) % len(perm)]  # wrap around to the first person
            total_happiness += happiness.get((person1, person2), 0)
            total_happiness += happiness.get((person2, person1), 0)
        max_happiness = max(max_happiness, total_happiness)

    return max_happiness

def main():
    lines = open_input_file()
    happiness = compute_happiness(lines)

    max_happiness = optimal_seating(happiness)
    print(max_happiness)

if __name__ == "__main__":
    main()