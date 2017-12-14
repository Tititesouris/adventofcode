hashString = input()


def decrypt(hashInput):
    lengths = list(map(ord, list(hashInput)))

    lengths.extend([17, 31, 73, 47, 23])

    size = 256
    elements = list(range(size))
    position = 0
    skip = 0

    for _ in range(64):
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

    denseHash = ""
    for i in range(size // 16):
        sparseHash = elements[i * 16]
        for j in range(1, 16):
            sparseHash = elements[i * 16 + j] ^ sparseHash
        denseHash += hex(sparseHash)[2:].zfill(2)

    return denseHash


used = 0
for i in range(128):
    binaryHash = str(bin(int(decrypt(hashString + "-" + str(i)), 16))[2:].zfill(128))
    for char in binaryHash:
        if char == "1":
            used += 1

print(used)