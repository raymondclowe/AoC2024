with open('day3.txt', 'r') as file:
    lines = file.read()

lines = lines.replace('\n', '')

import re

do_pattern = r'don\'t\(\).*?do\(\)'

clean_lines = re.sub(do_pattern,'',lines)

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

matches = re.findall(pattern, clean_lines)

# print(matches)

total = 0

for tup in matches:
    total += int(tup[0]) * int(tup[1] )

print(total)