list = []
while True:
    line = input()
    if line == "":
        break
    list.append(int(line))

jumps = 0
position = 0

while 0 <= position < len(list):
    last = position
    position += list[position]
    if list[last] >= 3:
        list[last] -= 1
    else:
        list[last] += 1
    jumps += 1

print(jumps)
