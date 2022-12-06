line = open("inputs/day6.txt", "r").read()

def find_marker_position(stream, length):
    for n in range(length, len(stream)):
        block = set(stream[n-length:n])
        if len(block) == length:
            return n

print("Part 1 solution:", find_marker_position(line, 4), "- Part 2 solution:", find_marker_position(line, 14))