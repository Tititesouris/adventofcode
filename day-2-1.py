file = []
while True:
    line = input()
    if line == "":
        break
    file.append(list(map(int, line.split())))

checksum = 0
for y in range(len(file)):
    minValue = 999999999
    maxValue = 0
    for x in range(len(file[y])):
        if file[y][x] < minValue:
            minValue = file[y][x]
        if file[y][x] > maxValue:
            maxValue = file[y][x]
    checksum += maxValue - minValue

print(checksum)