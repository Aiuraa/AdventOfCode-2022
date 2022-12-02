#
# AdventOfCode 2022 - Day 2
# By: Aiura using python
#

from enum import IntEnum

class Hand(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Game():
    possible_victories = {
        Hand.Rock: Hand.Scissors,
        Hand.Paper: Hand.Rock,
        Hand.Scissors: Hand.Paper
    }

    possible_loses = {
        Hand.Rock: Hand.Paper,
        Hand.Paper: Hand.Scissors,
        Hand.Scissors: Hand.Rock
    }

    def __init__(self, opponent_hands: str, your_hands: str):
        tok_you = {"X": Hand.Rock, "Y": Hand.Paper, "Z": Hand.Scissors}
        tok_opponent = {"A": Hand.Rock, "B": Hand.Paper, "C": Hand.Scissors}

        self.opponent = tok_opponent[opponent_hands]
        self.you = tok_you[your_hands]
        self.score = 0

    def calculate_match(self):
        # Draw
        if self.opponent == self.you:
            self.score = (3 + self.you)

        # Win!
        elif self.opponent == self.possible_victories[self.you]:
            self.score = (6 + self.you)

        # Lose
        else:
            self.score = self.you

        return self

    def modify_strategy(self):
        # Draw
        if self.you == Hand.Paper:
            self.you = self.opponent

        # Win
        elif self.you == Hand.Scissors:
            self.you = self.possible_loses[self.opponent]

        # Lose
        else:
            self.you = self.possible_victories[self.opponent]
            
        return self
    
    def results(self) -> int:
        return self.score

def parse_input(input_file: str) -> list:
    with open(input_file) as f:
        return f.read().strip().split("\n")

def part_one(rounds: list) -> int:
    scores = 0

    for hands in rounds:
        game = Game(hands[0], hands[2]).calculate_match()
        scores += game.results()

    return scores

def part_two(rounds: list) -> int:
    scores = 0

    for hands in rounds:
        game = Game(hands[0], hands[2]).modify_strategy().calculate_match()
        scores += game.results()
    
    return scores

def solve(input_file: str) -> None:
    input = parse_input(input_file)

    print("Part 1:")
    print(f"Results from game 1 is: {part_one(input)}")
    print("")
    print("Part 2:")
    print(f"Results from game 2 is: {part_two(input)}")

if __name__ == "__main__":
    solve("input.txt")
