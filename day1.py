#
# AdventOfCode 2022 - Day 1
# By: Aiuraa using python
#

def read_input() -> str:
    with open("input.txt") as f:
        output = f.read()
    
    # append for not getting false positive
    output += "\n"
    return output

def parse_input(a: str) -> list:
    sum_val = 0
    output = []
    tmp_val = ""

    for str_num in a:
        if str_num == '\n' and tmp_val == '':
            output.append(sum_val)
            sum_val = 0
            continue

        if str_num == '\n':
            sum_val += int(tmp_val)
            # Uncomment to see how summing works
            # print(f"Value: {int(tmp_val)} Sum: {sum_val}")
            tmp_val = ""
            continue

        if str_num != '':
            tmp_val += str_num

    return output

# Part 1
def find_answer_part_one(a: str) -> int:
    input = parse_input(a)
    return max(input)

def find_answer_part_two(a: str) -> int:
    output = parse_input(a)
    output.sort()

    print(f"Top 1: {output[-1]}")
    print(f"Top 2: {output[-2]}")
    print(f"Top 3: {output[-3]}")

    return (output[-1] + output[-2] + output[-3])



def main():
    print("---- [Part 1] ----")
    str_input = read_input()
    output_1 = find_answer_part_one(str_input)
    print(f"Biggest value is: {output_1}")

    print("---- [Part 2] ----")
    output_2 = find_answer_part_two(str_input)
    print(f"Combining results from top 3 is: {output_2}")

if __name__ == '__main__':
    main()
