"""
--- Day 17: No Such Thing as Too Much ---

The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

    15 and 10
    20 and 5 (the first 5)
    20 and 5 (the second 5)
    15, 5, and 5

Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

--- Part Two ---

While playing with all the containers in the kitchen, another load of eggnog arrives! The shipping and receiving department is requesting as many containers as you can spare.

Find the minimum number of containers that can exactly fit all 150 liters of eggnog. How many different ways can you fill that number of containers and still hold exactly 150 litres?

In the example above, the minimum number of containers was two. There were three ways to use that many containers, and so the answer there would be 3.
"""

def open_input_file():
    with open("2015/day-17/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

# my approach is to use a recursive function that takes the sorted list of containers, the target amount, and the current index in the list of containers. it will use the current index if possible, and then move on to the next index. if the target amount is 0, it will return 1, if the target amount is less than 0 or the index is out of bounds, it will return 0. otherwise, it will return the sum of the recursive calls with the current index and the next index.
def count_combinations(containers, target, index):
    if target == 0:
        return 1
    if target < 0 or index >= len(containers):
        return 0

    # if the target is greater than or equal to the current container, we can use it, so we call the function again with the target reduced by the current container and the same index, and also call the function again with the next index and the same target. we return the sum of these two calls.
    if target >= containers[index]:
        return count_combinations(containers, target - containers[index], index + 1) + count_combinations(containers, target, index + 1)
    # if the target is less than the current container, we can't use it, so we call the function again with the next index and the same target
    else:
        return count_combinations(containers, target, index + 1)
        

def find_min_containers(containers, target, index, current_count, min_count):
    if target == 0:
        if current_count == min_count:
            return 1
        else:
            return 0
    if target < 0 or index >= len(containers):
        return 0

    # if the target is greater than or equal to the current container, we can use it, so we call the function again with the target reduced by the current container and the same index, and also call the function again with the next index and the same target. we return the sum of these two calls.
    if target >= containers[index]:
        return find_min_containers(containers, target - containers[index], index + 1, current_count + 1, min_count) + find_min_containers(containers, target, index + 1, current_count, min_count)
    # if the target is less than the current container, we can't use it, so we call the function again with the next index and the same target
    else:
        return find_min_containers(containers, target, index + 1, current_count, min_count)


def main():
    lines = open_input_file()
    containers = sorted([int(line) for line in lines], reverse=True)
    target = 150

    # first we need to find the minimum number of containers that can exactly fit all 150 liters of eggnog. we can do this by calling the count_combinations function with the target and index 0, and keeping track of the current count of containers used. we will return the minimum count found.
    # we can do this by calling the count_combinations function with the target and index 0, and keeping track of the current count of containers used. we will return the minimum count found.
    min_count = float('inf')
    for i in range(len(containers)):
        count = find_min_containers(containers, target, 0, 0, i + 1)
        if count > 0:
            min_count = min(min_count, i + 1)

    # now that we have the minimum count, we can call the find_min_containers function again with the target and index 0, and keeping track of the current count of containers used. we will return the number of combinations that use the minimum count of containers.
    combinations = find_min_containers(containers, target, 0, 0, min_count)
    print(combinations)

if __name__ == "__main__":
    main()