phrases = []
while True:
    line = input()
    if line == "":
        break
    phrases.append(line.split())

count = 0


def are_anagrams(a, b):
    for i in range(len(a)):
        found = False
        for j in range(len(b) - 1, -1, -1):
            if a[i] == b[j]:
                b.pop(j)
                found = True
                break
        if not found:
            return False
    return b == []


def check_phrase(p):
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if are_anagrams(list(p[i]), list(p[j])):
                return False
    return True


for phrase in phrases:
    if check_phrase(phrase):
        count += 1

print(count)
