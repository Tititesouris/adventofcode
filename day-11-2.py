directions = input().split(",")


# ne,se,se,ne,n,nw,nw,s,s,s,s,nw,s,se,s,sw,nw,n,n,nw,n,se
def sign(a):
    if a > 0:
        return 1
    if a < 0:
        return -1
    return 0


maxDistance = 0
for i in range(len(directions)):
    subdir = directions[:i + 1]
    x = 0
    y = 0

    for direction in subdir:
        if direction == "n":
            y += 1
        if direction == "ne":
            x += 1
            y += 0.5
        if direction == "se":
            x += 1
            y -= 0.5
        if direction == "s":
            y -= 1
        if direction == "sw":
            x -= 1
            y -= 0.5
        if direction == "nw":
            x -= 1
            y += 0.5

    distance = 0
    while abs(x) > 0:
        if (abs(x) >= 2) or (y % 1 == 0.5):
            y -= 0.5 * sign(y)
        x -= sign(x)
        distance += 1
    distance += abs(y)
    if distance > maxDistance:
        maxDistance = distance

print(maxDistance)