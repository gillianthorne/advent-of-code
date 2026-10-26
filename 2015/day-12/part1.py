"""
--- Day 12: JSAbacusFramework.io ---

Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

    [1,2,3] and {"a":2,"b":4} both have a sum of 6.
    [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
    {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
    [] and {} both have a sum of 0.

You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?

"""
import json

def open_input_file():
    with open("2015/day-12/input.txt", "r", encoding="utf-8") as f:
        return f.read().strip()

def sum_numbers(data):
    # if the data is an integer, return it
    if isinstance(data, int):
        return data
    # if the data is a list, recursively sum the numbers in the list
    elif isinstance(data, list):
        return sum(sum_numbers(item) for item in data)
    # if the data is a dict, recursively sum the numbers in the values of the dict
    elif isinstance(data, dict):
        return sum(sum_numbers(value) for value in data.values())
    # otherwise, return 0 (for strings and other types - though we were told we won't encounter strings with numbers)
    else:
        return 0

def main():
    data = open_input_file()
    # parse the JSON data
    parsed_data = json.loads(data)
    total_sum = sum_numbers(parsed_data)
    print(total_sum)

if __name__ == "__main__":
    main()