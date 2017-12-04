phrases = []
while True:
    line = input()
    if line == "":
        break
    phrases.append(line.split())

count = 0


def check_phrase(p):
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] == p[j]:
                return False
    return True


for phrase in phrases:
    if check_phrase(phrase):
        count += 1

print(count)
