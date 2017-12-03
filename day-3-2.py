value = int(input())

memsize = 50
memory = [[0 for i in range(memsize)] for j in range(memsize)]

x = memsize // 2
y = memsize // 2
memory[y][x] = 1


def move(dir_x, dir_y):
    global x, y, memory
    x += dir_x
    y += dir_y
    memory[y][x] = sum([memory[y + j][x + i] for i in range(-1, 2) for j in range(-1, 2)])
    if memory[y][x] > value:
        return True
    return False


def get_value():
    global x, y
    n = 1
    while True:
        for i in range(n):
            if move(1, 0):
                return memory[y][x]
        for i in range(n):
            if move(0, 1):
                return memory[y][x]
        for i in range(n + 1):
            if move(-1, 0):
                return memory[y][x]
        for i in range(n + 1):
            if move(0, -1):
                return memory[y][x]
        n += 2


print(get_value())
