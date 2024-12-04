with open('day3.txt', 'r') as file:
    lines = file.read()

# lines = lines.replace('\n', '')

import re

pattern = r'mul\(\d{1,3},\d{1,3}\)|don\'t\(\)|do\(\)'

matches = re.findall(pattern, lines)

# print(matches)

total = 0

mulon = True

for blob in matches:
    if blob.startswith('mul'):
        if mulon:
            blob = blob.replace('mul(', '')
            blob = blob.replace(')', '')
            blob = blob.replace(',', ' ')
            tup = blob.split()
            total += int(tup[0]) * int(tup[1] )
        
    elif blob.startswith('don'):
        mulon = False
    elif blob.startswith('do()'):
        mulon = True
    

print(total)