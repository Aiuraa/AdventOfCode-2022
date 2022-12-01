#
# AdventOfCode 2022 - Day 1
# By: Aiuraa using python
#

def parse_input() -> list:
    sum_val = 0
    output = []

    with open("input/day1.txt") as f:
        for str_num in f.read().strip().split("\n"):
            if str_num == '':
                output.append(sum_val)
                sum_val = 0
                continue
            
            sum_val += int(str_num)

    return output

# Part 1
def find_answer_part_one(input: list) -> int:
    return max(input)

# Part 2
def find_answer_part_two(input: list) -> int:
    input.sort()

    print(f"Top 1: {input[-1]}")
    print(f"Top 2: {input[-2]}")
    print(f"Top 3: {input[-3]}")

    return (input[-1] + input[-2] + input[-3])

def main():
    calories = parse_input()

    print("---- [Part 1] ----")
    print(f"Biggest value is: {find_answer_part_one(calories)}")

    print("---- [Part 2] ----")
    print(f"Combining results from top 3 is: {find_answer_part_two(calories)}")

if __name__ == '__main__':
    main()
