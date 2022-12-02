#
# AdventOfCode 2022 - Day 1
# By: Aiuraa using python
#

def parse_input() -> list:
    sum_val = 0
    output = []

    with open("code/day1/input/day1.txt") as f:
        for str_num in f.read().strip().split("\n"):
            if str_num == '':
                output.append(sum_val)
                sum_val = 0
                continue
            
            sum_val += int(str_num)

    return output

# Part 1
def part_one() -> int:
    calories = parse_input()
    return max(calories)

# Part 2
def part_two() -> int:
    calories = parse_input()
    calories.sort()

    print(f"Top 1: {calories[-1]}")
    print(f"Top 2: {calories[-2]}")
    print(f"Top 3: {calories[-3]}")

    return (calories[-1] + calories[-2] + calories[-3])

def display():
    print("---- [Part 1] ----")
    print(f"Biggest value is: {part_one()}")
    print("")
    print("---- [Part 2] ----")
    print(f"Combining results from top 3 is: {part_two()}")

if __name__ == '__main__':
    display()
