lengths = list(map(int, input().split(",")))

size = 256
elements = list(range(size))
position = 0
skip = 0

for length in lengths:
    reverse = []
    for i in range(length):
        pos = (position + i) % size
        reverse.insert(0, elements[pos])
    for i in range(length):
        pos = (position + i) % size
        elements[pos] = reverse[i]
    position += length + skip
    skip += 1

print(elements[0] * elements[1])