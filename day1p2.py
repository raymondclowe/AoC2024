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

def how_many_times(list, number):
    count = 0
    for i in list:
        if i == number:
            count += 1
    return count

sim_score = 0
for i in range(len(a)):
    sim_score += a[i] *  how_many_times(b, a[i])

print(sim_score)
    


