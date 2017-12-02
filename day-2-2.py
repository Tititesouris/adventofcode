file = []
while True:
    line = input()
    if line == "":
        break
    file.append(list(map(int, line.split())))


def find_divisible(l):
    for a in range(len(l)):
        for b in range(len(l)):
            if l[a] > l[b] > 0 and l[a] % l[b] == 0:  # Apparently the two numbers to find can't be identical
                return l[a] // l[b]


checksum = 0
for y in range(len(file)):
    checksum += find_divisible(file[y])
print(checksum)
