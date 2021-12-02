##Determine the horizontal and depth position##

# 2d array of navigational course
with open('Day2\\course.txt', 'r') as file:
    course = [[str(n) for n in line.split()] for line in file]

##PART1##

horizontal = 0
depth = 0

for x in course:
    if x[0] == 'forward':
        horizontal += int(x[1])
    elif x[0] == 'up':
        depth -= int(x[1])
    elif x[0] == 'down':
        depth += int(x[1])

total_position = horizontal*depth

print(
    f"Horizontal position = {horizontal} and Depth = {depth}. Total position = {total_position}")


##PART2##

horizontal2 = 0
depth2 = 0
aim = 0

for x in course:
    if x[0] == 'forward':
        horizontal2 += int(x[1])
        depth2 += aim*int(x[1])
    elif x[0] == 'up':
        aim -= int(x[1])
    elif x[0] == 'down':
        aim += int(x[1])

total_position2 = horizontal2*depth2

print(
    f"Horizontal position = {horizontal2} and Depth = {depth2}. Total position = {total_position2}")
