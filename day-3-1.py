location = int(input())

x = 0
y = 0
position = 1


def move(dir_x, dir_y):
    global x, y, position
    x += dir_x
    y += dir_y
    position += 1
    if position == location:
        return True
    return False


def get_xy():
    global x, y, position
    n = 1
    if location == 0:
        return [0, 0]
    while True:
        for i in range(n):
            if move(1, 0):
                return [x, y]
        for i in range(n):
            if move(0, 1):
                return [x, y]
        for i in range(n + 1):
            if move(-1, 0):
                return [x, y]
        for i in range(n + 1):
            if move(0, -1):
                return [x, y]
        n += 2


xy = get_xy()
print(xy)
print(abs(xy[0]) + abs(xy[1]))