
#
# AdventOfCode 2022 - Day 5
# By: Aiura using python
#

def parse_input(input_file: str) -> list:
    with open(input_file) as f:
        input = f.read()[:-1].split("\n\n")

    return input

def get_instructions(input: list) -> list:
    ret = input[1].split("\n")
    return ret

def get_stack_map(input: list) -> list:
    max_stack = 0
    draw_maps = 0

    # Get Maps
    maps = input[0].split("\n")

    # Prepare stacks
    max_stack = int(max(maps[len(maps)-1][:-1]))
    stacks = [[] for _ in range(max_stack)]
    draw_maps = len(maps)-1

    # Draw maps
    for i in range(draw_maps):
        line = maps[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])
    
    return stacks

class CrateMover_9000():
    def __init__(self, stacks: list):
        self.stacks = [stack[::-1] for stack in stacks]
    
    def rearrange(self, instructions: list):
        for instruction in instructions:
            tok = instruction.split(" ")
            mov, where, to = map(int, [tok[1], tok[3], tok[5]])

            # Because how array index starts at 0, we need to decrement this to match with results.
            where -= 1
            to -= 1

            # Do the instructions here
            for _ in range(mov):
                # Swap once per crates
                val = self.stacks[where].pop()
                self.stacks[to].append(val)
        
        return self
    
    def results(self):
        top_stack = [stack[-1] for stack in self.stacks]
        return "".join(top_stack)

class CrateMover_9001():
    def __init__(self, stacks: list):
        self.stacks = [stack[::-1] for stack in stacks]
    
    def rearrange(self, instructions: list):
        for instruction in instructions:
            tok = instruction.split(" ")
            mov, where, to = map(int, [tok[1], tok[3], tok[5]])

            # Because how array index starts at 0, we need to decrement this to match with results.
            where -= 1
            to -= 1

            # Swap everything with the top thanks to extend
            self.stacks[to].extend(self.stacks[where][-mov:])
            self.stacks[where] = self.stacks[where][:-mov]
        
        return self
    
    def results(self):
        # Find top stacks
        top_stack = [stack[-1] for stack in self.stacks]
        return "".join(top_stack)

def solve(input_file: str) -> None:
    raw_input = parse_input(input_file)
    instruction = get_instructions(raw_input)

    print("Part 1:")
    print(f"CrateMover_9000 rearrangement results: {CrateMover_9000(get_stack_map(raw_input)).rearrange(instruction).results()}\n")
    
    print("Part 2:")
    print(f"CrateMover_9001 rearrangement results: {CrateMover_9001(get_stack_map(raw_input)).rearrange(instruction).results()}\n")
    
if __name__ == "__main__":
    solve("input.txt")
