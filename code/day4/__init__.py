
#
# AdventOfCode 2022 - Day 4
# By: Aiura using python
#

def parse_input(input_file: str) -> list:
    with open(input_file) as f:
        input = f.read().strip().split("\n")
    
    return input
    
def find_contained_assigment(input: str) -> int:
    ret = 0
    for assignment in input:
        assig1,assig2 = [something.split("-") for something in assignment.split(",")]
        a,b,c,d = map(int, [assig1[0], assig1[1], assig2[0], assig2[1]])

        if a <= c and b >= d or a >= c and b <= d:
            # print(f"Found it, it was assigment no: {a}-{b} and {c}-{d}")
            ret += 1
    
    return ret

def find_overlap_assigment(input: str) -> int:
    ret = 0
    for assignment in input:
        assig1, assig2 = [x.split("-") for x in assignment.split(",")]
        a,b,c,d = map(int, [assig1[0], assig1[1], assig2[0], assig2[1]])

        if not (b < c or a > d):
            # print(f"Found it, it was assigment no: {a}-{b} and {c}-{d}")
            ret += 1
        
    return ret

def solve(input_file: str) -> None:
    input = parse_input(input_file)

    print("Part 1:")
    print(f"Total contained assigment is: {find_contained_assigment(input)}\n")
    
    print("Part 2:")
    print(f"total overlapping assigment is: {find_overlap_assigment(input)}\n")
    
if __name__ == "__main__":
    solve("input.txt")
