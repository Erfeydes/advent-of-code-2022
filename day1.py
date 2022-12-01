lines = open("inputs/day1.txt", "r").read().split("\n\n")
total_calories = sorted([sum([int(x) for x in line.split("\n")]) for line in lines], reverse=True)

print("Part 1 solution:", total_calories[0], "- Part 2 solution:", sum(total_calories[:3]))