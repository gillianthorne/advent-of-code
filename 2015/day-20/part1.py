"""
--- Day 20: Infinite Elves and Infinite Houses ---

To keep the Elves busy, Santa has them deliver some presents by hand, door-to-door. He sends them down a street with infinite houses numbered sequentially: 1, 2, 3, 4, 5, and so on.

Each Elf is assigned a number, too, and delivers presents to houses based on that number:

    The first Elf (number 1) delivers presents to every house: 1, 2, 3, 4, 5, ....
    The second Elf (number 2) delivers presents to every second house: 2, 4, 6, 8, 10, ....
    Elf number 3 delivers presents to every third house: 3, 6, 9, 12, 15, ....

There are infinitely many Elves, numbered starting with 1. Each Elf delivers presents equal to ten times his or her number at each house.

So, the first nine houses on the street end up like this:

House 1 got 10 presents.
House 2 got 30 presents.
House 3 got 40 presents.
House 4 got 70 presents.
House 5 got 60 presents.
House 6 got 120 presents.
House 7 got 80 presents.
House 8 got 150 presents.
House 9 got 130 presents.

The first house gets 10 presents: it is visited only by Elf 1, which delivers 1 * 10 = 10 presents. The fourth house gets 70 presents, because it is visited by Elves 1, 2, and 4, for a total of 10 + 20 + 40 = 70 presents.

What is the lowest house number of the house to get at least as many presents as the number in your puzzle input?

Your puzzle input is 29000000.

--- Part Two ---

The Elves decide they don't want to visit an infinite number of houses. Instead, each Elf will stop after delivering presents to 50 houses. To make up for it, they decide to deliver presents equal to eleven times their number at each house.

With these changes, what is the new lowest house number of the house to get at least as many presents as the number in your puzzle input?
"""

def main():
    target = 29000000
    # brute force doesn't really work, so i'm going to use a sieve approach. for each elf, i'm going to add 11 times their number to each house they visit. then i'll check each house to see if it has at least the target number of presents.

    # except that changing "10" to "11" doesn't work and limiting it to 50 houses doesn't work because it stops too early. i need to increase the number of houses to check but i don't want to brute force it. i can use the fact that the number of presents at each house is equal to the sum of the divisors of the house number times 11. so i can use a sieve to find the sum of the divisors for each house number up to a certain limit, and then multiply by 11 and check if it's greater than or equal to the target.
    houses = [0] * (target // 11)  # create a list of houses, each initialized to 0 presents
    for elf in range(1, len(houses)):
        # from elf to either the end of the houses list or elf * 50, whichever is smaller, step by elf (so that each elf only visits 50 houses)
        for house in range(elf, min(len(houses), elf * 50 + 1), elf): 
            houses[house] += elf * 11  # each elf delivers 11 times their number of presents to each house they visit

    for house, presents in enumerate(houses):
        if presents >= target:
            print(house)
            break


if __name__ == "__main__":
    main()