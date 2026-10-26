"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas. It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking. The player always goes first. Each attack reduces the opponent's hit points by at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points. If the defender had an armor score of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. You have 100 hit points.

Here is what the item shop is selling:

Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

    The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
    The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
    The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.

In this scenario, the player wins! (Barely.)

You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?
"""
from itertools import combinations

def open_input_file():
    with open("2015/day-21/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def get_weapon_stats():
    return {
        "Dagger": (8, 4, 0),
        "Shortsword": (10, 5, 0),
        "Warhammer": (25, 6, 0),
        "Longsword": (40, 7, 0),
        "Greataxe": (74, 8, 0)
    }

def get_armor_stats():
    return {
        "Leather": (13, 0, 1),
        "Chainmail": (31, 0, 2),
        "Splintmail": (53, 0, 3),
        "Bandedmail": (75, 0, 4),
        "Platemail": (102, 0, 5)
    }

def get_ring_stats():
    return {
        "Damage +1": (25, 1, 0),
        "Damage +2": (50, 2, 0),
        "Damage +3": (100, 3, 0),
        "Defense +1": (20, 0, 1),
        "Defense +2": (40, 0, 2),
        "Defense +3": (80, 0, 3)
    }

def get_boss_stats(lines):
    boss_stats = {}
    for line in lines:
        parts = line.split(": ")
        stat_name = parts[0].lower()
        stat_value = int(parts[1])
        boss_stats[stat_name] = stat_value
    return boss_stats

def get_player_stats(weapon, armor, rings):
    weapon_cost, weapon_damage, weapon_armor = weapon
    armor_cost, armor_damage, armor_armor = armor
    ring_costs, ring_damages, ring_armors = zip(*rings) if rings else ([], [], [])
    
    total_cost = weapon_cost + armor_cost + sum(ring_costs)
    total_damage = weapon_damage + armor_damage + sum(ring_damages)
    total_armor = weapon_armor + armor_armor + sum(ring_armors)
    
    return (100, total_damage, total_armor), total_cost  # Player has 100 hit points

def calculate_damage(attacker_damage, defender_armor):
    return max(1, attacker_damage - defender_armor)

def simulate_battle(player_stats, boss_stats):
    player_hp, player_damage, player_armor = player_stats
    boss_hp, boss_damage, boss_armor = boss_stats

    while True:
        # Player attacks first
        damage_to_boss = calculate_damage(player_damage, boss_armor)
        boss_hp -= damage_to_boss
        if boss_hp <= 0:
            return True  # Player wins

        # Boss attacks
        damage_to_player = calculate_damage(boss_damage, player_armor)
        player_hp -= damage_to_player
        if player_hp <= 0:
            return False  # Boss wins

def calculate_min_cost_to_win(boss_stats):
    weapons = get_weapon_stats()
    armor = [(0, 0, 0), *get_armor_stats().values()]
    rings = get_ring_stats()

    min_cost = float('inf')
    # this is a lot of nested loops, but it's only 5 * 6 * (1 + 6 + 15) = 5 * 6 * 22 = 660 combinations, which is fine. we can also use itertools.combinations to get the ring combinations.
    # 1 + 6 + 15 = 22 because we can choose 0, 1, or 2 rings from the 6 available rings. choosing 0 rings is 1 way, choosing 1 ring is 6 ways, and choosing 2 rings is C(6,2) = 15 ways.
    for weapon_name, weapon_stats in weapons.items():
        for armor_stats in armor:
            for num_rings in range(3):  # 0, 1, or 2 rings
                for ring_combination in combinations(rings.values(), num_rings):
                    player_stats, total_cost = get_player_stats(weapon_stats, armor_stats, ring_combination)
                    if simulate_battle(player_stats, (boss_stats['hit points'], boss_stats['damage'], boss_stats['armor'])):
                        # on the end of the loop, overwrite the min_cost variable with the total_cost if it's less than the current min_cost
                        # could also be "if total_cost < min_cost: min_cost = total_cost" but this is more explicit
                        min_cost = min(min_cost, total_cost)

    return min_cost

def calculate_max_cost_to_lose(boss_stats):
    weapons = get_weapon_stats()
    armor = [(0, 0, 0), *get_armor_stats().values()]
    rings = get_ring_stats()

    max_cost = float('-inf')
    # this is a lot of nested loops, but it's only 5 * 6 * (1 + 6 + 15) = 5 * 6 * 22 = 660 combinations, which is fine. we can also use itertools.combinations to get the ring combinations.
    # 1 + 6 + 15 = 22 because we can choose 0, 1, or 2 rings from the 6 available rings. choosing 0 rings is 1 way, choosing 1 ring is 6 ways, and choosing 2 rings is C(6,2) = 15 ways.
    for weapon_name, weapon_stats in weapons.items():
        for armor_stats in armor:
            for num_rings in range(3):  # 0, 1, or 2 rings
                for ring_combination in combinations(rings.values(), num_rings):
                    player_stats, total_cost = get_player_stats(weapon_stats, armor_stats, ring_combination)
                    if not simulate_battle(player_stats, (boss_stats['hit points'], boss_stats['damage'], boss_stats['armor'])):
                        # on the end of the loop, overwrite the max_cost variable with the total_cost if it's greater than the current max_cost
                        # could also be "if total_cost > max_cost: max_cost = total_cost" but this is more explicit
                        max_cost = max(max_cost, total_cost)

    return max_cost

def main():
    lines = open_input_file()
    boss_stats = get_boss_stats(lines)
    max_cost = calculate_max_cost_to_lose(boss_stats)
    print(max_cost)

if __name__ == "__main__":
    main()