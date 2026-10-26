"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---

Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

For example:

    ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
    aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
    jchzalrnumimnmhp is naughty because it has no double letter.
    haegwjzuvuyypxyu is naughty because it contains the string xy.
    dvszwmarrgswjxmb is naughty because it contains only one vowel.
"""

def open_input_file():
    with open("2015/day-5/input.txt") as f:
        return f.read().splitlines()

def vowel_check(s):
    vowels = set("aeiouAEIOU")

    vowel_count = sum(1 for char in s if char in vowels)

    if vowel_count >= 3:
        return True

    return False

def double_letter_check(s):
    previous_char = ""
    for char in s:
        if char == previous_char:
            return True
        previous_char = char

    return False

def bad_string_check(s):
    bad_strings = ["ab", "cd", "pq", "xy"]
    for string in bad_strings:
        if string in s:
            return False

    return True

def main():
    instructions = open_input_file()

    count = 0
    for row in instructions:
        if vowel_check(row) and double_letter_check(row) and bad_string_check(row):
            count += 1

    print(count)

if __name__ == "__main__":
    main()