"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

    Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

def open_input_file():
    with open("2015/day-14/input.txt", "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f]
    return lines

def get_reindeer(lines):
    reindeer = {}
    for line in lines:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer[name] = (speed, fly_time, rest_time)
    return reindeer

def calculate_distance(reindeer, time):
    speed, fly_time, rest_time = reindeer
    
    # how long it takes him to complete one full cycle of flying and resting
    cycle_time = fly_time + rest_time

    # how many full cycles he can complete in the given time, and how much time is left over after those full cycles
    full_cycles = time // cycle_time
    remaining_time = time % cycle_time
    
    # however many full cycles, plus the remaining time or fly time, whichever is less (either the rest of the remaining time if it ends before his rest period, or the full fly time if he can fly the whole remaining time)
    distance = full_cycles * speed * fly_time + min(remaining_time, fly_time) * speed
    
    return distance

def main():
    lines = open_input_file()
    reindeer = get_reindeer(lines)
    time = 2503
    distances = {name: calculate_distance(stats, time) for name, stats in reindeer.items()}
    winning_distance = max(distances.values())
    print(winning_distance)

if __name__ == "__main__":
    main()