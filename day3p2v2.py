with open('day3.txt', 'r') as file:
    lines = file.read()

# lines = lines.replace('\n', '')

import re

pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'

matches = re.findall(pattern, lines)

# print(matches)

total = 0

mul_is_on = True

for match in matches:
    if match.startswith('mul'):
        if mul_is_on:
            match = match.replace('mul(', '')
            match = match.replace(')', '')
            match = match.replace(',', ' ')
            tup = match.split()
            total += int(tup[0]) * int(tup[1] )
        
    elif match.startswith('don'):
        mul_is_on = False
    elif match.startswith('do()'):
        mul_is_on = True
    

print(total)