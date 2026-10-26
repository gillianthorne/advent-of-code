"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

    123 -> x means that the signal 123 is provided to wire x.
    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.

Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
"""

def open_input_file():
    with open("2015/day-7/input.txt") as f:
        return f.read().splitlines()

def resolve_value(value, instructions, wires):
    # takes one value (string, either wire or number) and returns an integer value
    if value.isdigit():
        return int(value)
    # check if the value has already been resolved
    elif value in wires:
        return wires[value]
    else:
        # recursively resolve the value of the wire
        instruction = instructions[value]
        # split the text into tokens on whitespace
        tokens = instruction.split()
        # if the instruction is a single value, return that value
        if len(tokens) == 1:
            resolved_value = resolve_value(tokens[0], instructions, wires)
            wires[value] = resolved_value
            return resolved_value
        # if it's 2 tokens, it's a NOT operation
        elif len(tokens) == 2:
            resolved_value = ~resolve_value(tokens[1], instructions, wires) & 0xFFFF
            wires[value] = resolved_value
            return resolved_value
        # if it's 3 tokens, it's a binary operation
        elif len(tokens) == 3:
            left = resolve_value(tokens[0], instructions, wires)
            right = resolve_value(tokens[2], instructions, wires)
            if tokens[1] == "AND":
                resolved_value = left & right
            elif tokens[1] == "OR":
                resolved_value = left | right
            elif tokens[1] == "LSHIFT":
                resolved_value = (left << right) & 0xFFFF
            elif tokens[1] == "RSHIFT":
                resolved_value = left >> right
            wires[value] = resolved_value
            return resolved_value


def main():
    instructions = open_input_file()
    # split the instructions on the "->" symbol and store them in a dictionary
    instruction_dict = {}
    for row in instructions:
        parts = row.split(" -> ")
        if len(parts) == 2:
            instruction_dict[parts[1]] = parts[0]

    instruction_dict["b"] = "3176"

    print(resolve_value("a", instruction_dict, {}))
    resolved_a = 3176
    print(resolved_a)


if __name__ == "__main__":
    main()