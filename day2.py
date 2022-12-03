lines = open("inputs/day2.txt", "r").read().split("\n")

score = {
    "A X": 1+3,
    "A Y": 2+6,
    "A Z": 3+0,
    "B X": 1+0,
    "B Y": 2+3,
    "B Z": 3+6,
    "C X": 1+6,
    "C Y": 2+0,
    "C Z": 3+3
}

strategy = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X"
}

def get_total_score(func):
    return sum(map(func, lines))

def get_round_score_with_strategy(line):
    return score[strategy.get(line)]

print("Part 1 solution:", get_total_score(score.get), "- Part 2 solution:", get_total_score(get_round_score_with_strategy))