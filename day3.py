lines = open("inputs/day3.txt", "r").read().rsplit()

def get_priorities_sum(letters):
    return sum([ord(letter)-38 if str.isupper(letter) else ord(letter)-96 for letter in letters])

def find_errors():
    return [list(set(l[:len(l)//2]) & set(l[len(l)//2:]))[0] for l in lines]

def find_badges():
    return [list(set(l1) & set(l2) & set(l3))[0] for l1, l2, l3 in [lines[i:i+3] for i in range (0, len(lines), 3)]]

print("Part 1 solution:", get_priorities_sum(find_errors()), "- Part 2 solution:", get_priorities_sum(find_badges()))