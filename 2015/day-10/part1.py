"""
--- Day 10: Elves Look, Elves Say ---

Today, the Elves are playing a game called look-and-say. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, 211 is read as "one two, two ones", which becomes 1221 (1 2, 2 1s).

Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like 111) with the number of digits (3) followed by the digit itself (1).

For example:

    1 becomes 11 (1 copy of digit 1).
    11 becomes 21 (2 copies of digit 1).
    21 becomes 1211 (one 2 followed by one 1).
    1211 becomes 111221 (one 1, one 2, and two 1s).
    111221 becomes 312211 (three 1s, two 2s, and one 1).

Starting with the digits in your puzzle input, apply this process 40 times. What is the length of the result?

--- Part Two ---

Neat, right? You might also enjoy hearing John Conway talking about this sequence (that's Conway of Conway's Game of Life fame).

Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?
"""

def digit_count(input_string):
    # iterate through the input string and count the number of consecutive digits
    output_string = ""
    index = 0
    output_array = []

    while index < len(input_string):
        j = index
        # count the number of consecutive digits
        while j < len(input_string) and input_string[j] == input_string[index]:
            j += 1

        count = j - index
        # get the current digit
        current_digit = input_string[index]
        # append the count and the digit to the arrau
        output_array.append(str(count))
        output_array.append(current_digit)

        # set the index to the next digit
        index = j
        
    # join the output array into a string
    output_string = "".join(output_array)
    return output_string

def main():
    input_string = "3113322113"

    for _ in range(50):
        output_string = digit_count(input_string)
        print(f"Iteration {_ + 1}: {len(output_string)}")
        input_string = output_string

    print(len(output_string))

if __name__ == "__main__":
    main()