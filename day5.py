import re

lines = open("inputs/day5.txt", "r").readlines()
lines = [d.replace("\n","") for d in lines]

def clean_input():
    stack_input = lines[:8]
    stack_input = [l.replace("    ", "-") for l in stack_input]
    stacks = [[] for _ in range(9)]

    for l in reversed(stack_input):
        stack = 0
        for car in l:
            if 64 < ord(car) < 91:
                stacks[stack].append(car)
                stack += 1
            elif car == "-":
                stack += 1

    moves = [re.findall(r"\d+", l) for l in lines[10:]]
    moves = [[int(v) for v in m] for m in moves]

    return stacks, moves

def display_top_crates(stacks):
    result = ""
    for s in stacks:
        result += s[-1]
    return result

def move_crates_9000():
    stacks, moves = clean_input()
    for move in moves:
        n, f, t = move #number, from, to
        for i in range(n):
            stacks[t-1].append(stacks[f-1].pop())
    return stacks

def move_crates_9001():
    stacks, moves = clean_input()
    for move in moves:
        n, f, t = move
        crates = stacks[f-1][-n:]

        for crate in crates:
            stacks[f-1].pop()
            stacks[t-1].append(crate)
    return stacks

print("Part 1 solution:", display_top_crates(move_crates_9000()), "- Part 2 solution:", display_top_crates(move_crates_9001()))