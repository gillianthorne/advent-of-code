"""
--- Day 9: All in a Single Night ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141

The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""
from itertools import permutations

def open_input_file():
    with open("2015/day-9/input.txt", "r", encoding="utf-8") as f:
        return f.read().splitlines()

def parse_input(lines):
    distances = {}
    for line in lines:
        parts = line.split()
        city1 = parts[0]
        city2 = parts[2]
        distance = int(parts[4])
        distances[(city1, city2)] = distance
        distances[(city2, city1)] = distance  # Add reverse direction

    return distances

def main():
    lines = open_input_file()
    distances = parse_input(lines)
    # find the shortest route that hits all cities exactly once
    cities = set()
    for city1, city2 in distances.keys():
        cities.add(city1)
        cities.add(city2)

    print(f"Cities: {cities}")

    longest_distance = float('-inf')
    for perm in permutations(cities):
        total_distance = 0
        for i in range(len(perm) - 1):
            total_distance += distances[(perm[i], perm[i + 1])]
        longest_distance = max(longest_distance, total_distance)

    print(f"Longest distance: {longest_distance}")

if __name__ == "__main__":
    main()