from enum import IntEnum

class Token(IntEnum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Parser():
    possible_victories = {
        Token.Rock: Token.Scissors,
        Token.Paper: Token.Rock,
        Token.Scissors: Token.Paper
    }

    possible_loses = {
        Token.Rock: Token.Paper,
        Token.Paper: Token.Scissors,
        Token.Scissors: Token.Rock
    }

    def __init__(self, input: str):
        tok_you = {"X": Token.Rock, "Y": Token.Paper, "Z": Token.Scissors}
        tok_opponent = {"A": Token.Rock, "B": Token.Paper, "C": Token.Scissors}

        self.opponent = Token(tok_opponent[input[0]])
        self.you = Token(tok_you[input[2]])
        self.score = 0

    def calculate_match(self):
        if self.opponent == self.you:
            self.score = (3 + self.you)
        elif self.opponent == self.possible_victories[self.you]:
            self.score = (6 + self.you)
        else:
            self.score = self.you

        return self

    def modify_strategy(self):
        # Insta win
        if self.you == Token.Scissors:
            self.you = self.possible_loses[self.opponent]

        # Draw
        elif self.you == Token.Paper:
            self.you = self.opponent

        # Lose
        else:
            self.you = self.possible_victories[self.opponent]
            
        return self
    
    def results(self) -> int:
        return self.score

def parse_input() -> list:
    with open("code/day2/input/day2.txt") as f:
        return f.read().strip().split("\n")

def part_one() -> int:
    rounds = parse_input()
    scores = 0

    for battle in rounds:
        game = Parser(battle).calculate_match()
        scores += game.results()

    return scores

def part_two() -> int:
    rounds = parse_input()
    scores = 0

    for battle in rounds:
        game = Parser(battle).modify_strategy().calculate_match()
        scores += game.results()
    
    return scores

def display() -> None:
    print("---- [Part 1] ----")
    print(f"Results from game 1 is: {part_one()}")
    print("")
    print("---- [Part 2] ----")
    print(f"Results from game 2 is: {part_two()}")

if __name__ == '__main__':
    display()
