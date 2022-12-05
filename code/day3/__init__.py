#
# AdventOfCode 2022 - Day 3
# By: Aiura using python
#

from string import ascii_lowercase, ascii_uppercase

def parse_input(input_file: str) -> list:
    with open(input_file) as f:
        return f.read().strip().split("\n")

# Part one
def find_items(input: list) -> int:
    keys = ascii_lowercase + ascii_uppercase
    output = 0
    
    for items in input:
        length = len(items)

        first_half = items[:(length//2)]
        second_half = items[(length//2):]

        for idx, key in enumerate(keys):
            if key in first_half and key in second_half:
                output += keys.index(key) + 1

    return output

# Part two
def find_item_stickers(input: list) -> int:
    keys = ascii_lowercase + ascii_uppercase
    output = 0

    for idx in range(0, len(input), 3):
        stack = input[idx:(idx + 3)] # get 3 stack of items

        for i, char in enumerate(keys):
            if all([char in char_list for char_list in stack]):
                output += keys.index(char) + 1

    return output

def solve(input_file: str) -> None:
    inventory = parse_input(input_file)
    
    print("Part 1:")
    print(f"The sum in both compartments of rucksack is: {find_items(inventory)}\n")

    print("Part 2:")
    print(f"The sum for ruckstack badge sticker is: {find_item_stickers(inventory)}\n")

if __name__ == "__main__":
    solve("input.txt")