stream = input()

score = 0
ignore = False
garbage = False
opened = 0

for c in stream:
    if not ignore:
        if c == '>':
            garbage = False
        elif c == '!':
            ignore = True
        elif garbage:
            score += 1

        if not garbage:
            if c == '{':
                opened += 1
            elif c == '}':
                opened -= 1
            elif c == '<':
                garbage = True
    else:
        ignore = False

print(score)
