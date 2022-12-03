#
# AdventOfCode 2022 - Day 1
# By: Aiura using python
#

def parse_input(input_file: str) -> list:
    sum_val = 0
    output = []

    with open(input_file) as f:
        for str_num in f.read().strip().split("\n"):
            if str_num == '':
                output.append(sum_val)
                sum_val = 0
                continue
            
            sum_val += int(str_num)

    return output

# Part 1
def part_one(calories: list) -> int:
    return max(calories)

# Part 2
def part_two(calories: list) -> int:
    calories.sort()

    print(f"Top 1: {calories[-1]}")
    print(f"Top 2: {calories[-2]}")
    print(f"Top 3: {calories[-3]}")

    return (calories[-1] + calories[-2] + calories[-3])

def solve(input_file: str) -> None:
    calories = parse_input(input_file)

    print("Part 1:")
    print(f"Biggest value is: {part_one(calories)}\n")

    print("Part 2:")
    print(f"Combining results from top 3 is: {part_two(calories)}\n")

if __name__ == "__main__":
    solve("input.txt")
