char_array = []

with open('day4.txt', 'r') as file:
    for line in file:
        # Strip the newline and convert the line into a list of characters
        char_array.append(list(line.strip()))

def get_char(x,y):
    if x < 0 or y < 0:
        return ' '
    try:
        return char_array[x][y]
    except IndexError:
        return ' '

def extract_string(x, y, rotation):
    # rotation 1 is left to right, rotation 2 is diagonal down, rotation 3 is down

    if rotation == 1: # ->
        xoffset, yoffset = 0, 1
    if rotation == 2: # \
        xoffset, yoffset = 1, 1
    if rotation == 3: # |
        xoffset, yoffset = 1, 0
    if rotation == 4: # /
        xoffset, yoffset = -1, 1
    if rotation == 5: # <-
        xoffset, yoffset = 0, -1
    if rotation == 6: # /
        xoffset, yoffset = -1, -1
    if rotation == 7: # |
        xoffset, yoffset = -1, 0
    if rotation == 8:
        xoffset, yoffset = 1, -1

    result = get_char(x,y)
    for i in range(1, 4):
        x += xoffset
        y += yoffset
        result += get_char(x,y)

    return result


xmas_count = 0
for x in range(0, len(char_array)):
    for y in range(0, len(char_array[x])):
        for i in range(1, 9):
            if extract_string(x, y, i) == "XMAS":
                xmas_count += 1
print(xmas_count)
    
    
