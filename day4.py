import re

filename = "inputs/day4.txt"
lines = [list(map(int, re.split(",|-", line.rstrip()))) for line in open(filename).read().rsplit()]

def create_sets(line):
    e1 = set([n for n in range(line[0], line[1]+1)])
    e2 = set([n for n in range(line[2], line[3]+1)])
    return [e1, e2]

sets = [create_sets(line) for line in lines]

def is_fully_contained():
    return [1 if s[0].issubset(s[1]) or s[1].issubset(s[0]) else 0 for s in sets]

def is_overlapping():
    return [1 if not s[0].isdisjoint(s[1]) else 0 for s in sets]

print("Part 1 solution:", sum(is_fully_contained()), "- Part 2 solution:", sum(is_overlapping()))