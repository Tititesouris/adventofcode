banks = list(map(int, input().split()))

cycles = 0
states = []


def has_repeated():
    for state in states:
        if state == banks:
            return True
    return False


while not has_repeated():
    states.append(banks[:])
    pos = 0
    val = 0
    for i in range(len(banks)):
        if banks[i] > val:
            val = banks[i]
            pos = i
    banks[pos] = 0
    pos = (pos + 1) % len(banks)
    while val > 0:
        banks[pos] += 1
        val -= 1
        pos = (pos + 1) % len(banks)
    cycles += 1

print(cycles)