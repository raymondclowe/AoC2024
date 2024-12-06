with open("day5.txt") as f:
    lines = f.readlines()

rules = []
updates = []

switch = False

for line in lines:
    print(line)
    if line == '\n':
        switch = True
        continue
    if not switch:
        rule_lst = [int(x) for x in line.strip().split('|')]
        rules.append(rule_lst)
    else:
        updates.append( [int(x) for x in line.strip().split(',')])

print(rules)
print(updates)
print ('done')

def conforms_to_rule(update, rule):
    
    if not ((rule[0] in update) and (rule[1] in update)):
        return True
    
    pos_left_part = update.index(rule[0])
    pos_right_part = update.index(rule[1])
    if pos_left_part > pos_right_part:
        return False
    return True

def  update_valid(update):
    for rule in rules:
        if not conforms_to_rule(update, rule):
            return False
    return True

total = 0
for update in updates:
    if update_valid(update):
        print(f'valid: {update}')
        middle_value_of_update = update[len(update)//2]
        total += middle_value_of_update
    else:
        print(f'invalid: {update}')

print(f'total: {total}')