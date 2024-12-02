with open('day1.txt', 'r') as file:
    lines = file.readlines()

a = []
b = []

for line in lines:
    splitted = line.split()
    a.append(int(splitted[0]))
    b.append(int(splitted[1]))

a.sort()
b.sort()

total_differences = 0
for i in range(len(a)):
    
    difference_between = abs(a[i] - b[i])
    print(a[i], b[i], difference_between)
    total_differences += difference_between

print(total_differences)


