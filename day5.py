with open("day5-example.txt") as f:
    lines = f.readlines()

rules = []
updates = []

switch = False

for line in lines:
    if line == '\n':
        switch = True
        continue
    if switch:
        updates.append(line.strip())
    else:
        rules.append( [int(x) for x in line.strip().split(',')])

print(rules)
print(updates)
print ('done')