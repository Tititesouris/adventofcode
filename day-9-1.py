stream = input()

score = 0
ignore = False
garbage = False
opened = 0

for c in stream:
    if not ignore:
        if not garbage:
            if c == '{':
                opened += 1
            elif c == '}':
                score += opened
                opened -= 1
            elif c == '<':
                garbage = True
        if c == '>':
            garbage = False
        elif c == '!':
            ignore = True
    else:
        ignore = False

print(score)
