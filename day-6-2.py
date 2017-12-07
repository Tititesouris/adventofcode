banks = list(map(int, input().split()))

cycles = -1
states = []


def last_repeated():
    i = 0
    for state in states:
        if state == banks:
            return i
        i += 1
    return -1


while cycles == -1:
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
    cycles = last_repeated()

print(len(states) - cycles)
