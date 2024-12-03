with open('day3.txt', 'r') as file:
    lines = file.read()

# print(lines)

import re

pattern = r'mul\((\d+),(\d+)\)'

matches = re.findall(pattern, lines)

print(matches)

total = 0

for tup in matches:
    total += int(tup[0]) * int(tup[1] )

print(total)