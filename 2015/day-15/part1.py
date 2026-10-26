"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

    capacity (how well it helps the cookie absorb milk)
    durability (how well it keeps the cookie intact when full of milk)
    flavor (how tasty it makes the cookie)
    texture (how it improves the feel of the cookie)
    calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

    A capacity of 44*-1 + 56*2 = 68
    A durability of 44*-2 + 56*3 = 80
    A flavor of 44*6 + 56*-2 = 152
    A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""

def open_input_file():
    with open("2015/day-15/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def get_ingredients(lines):
    ingredients = {}
    for line in lines:
        parts = line.split()
        name = parts[0][:-1] # (remove the colon at the end of the name)
        capacity = int(parts[2][:-1]) # (remove the comma at the end of the number)
        durability = int(parts[4][:-1]) # (remove the comma at the end of the number)
        flavor = int(parts[6][:-1]) # (remove the comma at the end
        texture = int(parts[8][:-1]) # (remove the comma at the end of the number)
        calories = int(parts[10]) # (no comma at the end of the number)
        ingredients[name] = (capacity, durability, flavor, texture, calories)

    return ingredients

def calculate_score(ingredients, amounts):
    # total score of the cookie is the sum of each of the properties, then multiplied together (ignoring calories)
    # sum (value * amount) for every ingredient
    total_capacity = sum(ingredients[name][0] * amount for name, amount in amounts.items())
    total_durability = sum(ingredients[name][1] * amount for name, amount in amounts.items())
    total_flavor = sum(ingredients[name][2] * amount for name, amount in amounts.items()) 
    total_texture = sum(ingredients[name][3] * amount for name, amount in amounts.items())

    # if any of the totals are negative, they become 0
    total_capacity = max(total_capacity, 0)
    total_durability = max(total_durability, 0)
    total_flavor = max(total_flavor, 0)
    total_texture = max(total_texture, 0)

    # the total score is the product of the totals (ignoring calories)
    total_score = total_capacity * total_durability * total_flavor * total_texture

    return total_score


def generate_combinations(ingredients, amounts, remaining, index):
    if remaining == 0:
        # we have used exactly 100 teaspoons of ingredients, so we can calculate the score of this combination
        score = calculate_score(ingredients, amounts)
        return score

    if index >= len(ingredients):
        # we have used all ingredients, but we haven't used exactly 100 teaspoons of ingredients, so this combination is invalid
        return 0

    # get the name of the ingredient at the current index, and the maximum amount we can use of this ingredient (which is the remaining amount of teaspoons we have left to use)
    name = list(ingredients.keys())[index]
    max_amount = remaining

    # try all possible amounts of this ingredient, from 0 to the remaining amount
    best_score = 0
    for amount in range(max_amount + 1):
        amounts[name] = amount
        score = generate_combinations(ingredients, amounts, remaining - amount, index + 1)
        best_score = max(best_score, score)

    return best_score

def main():
    lines = open_input_file()
    ingredients = get_ingredients(lines)
    amounts = {}
    best_score = generate_combinations(ingredients, amounts, 100, 0)
    print(best_score)

if __name__ == "__main__":
    main()