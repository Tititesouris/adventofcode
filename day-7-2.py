raw_programs = []
while True:
    line = input()
    if line == "":
        break
    parts = line.split()[:]
    name = parts[0]
    weight = int(parts[1][1:-1])
    children = []
    for child in parts[3:]:
        children.append(child.strip(","))
    raw_programs.append([name, weight, children])


def get_root():
    for program in raw_programs:
        seen = False
        for p in raw_programs:
            if program[0] in p[2]:
                seen = True
                break
        if not seen:
            return program
    return None


def get_pgrm(name):
    for program in raw_programs:
        if program[0] == name:
            return program
    return None


def inspect(node):
    weights = []
    if node[2] != []:
        for child in node[2]:
            weights.append(inspect(get_pgrm(child)))

        if weights.count(min(weights)) == 1:
            incorrect = min(weights)
            difference = max(weights) - incorrect
        else:
            incorrect = max(weights)
            difference = min(weights) - incorrect

        if difference != 0:
            i = 0
            for weight in weights:
                if weight == incorrect:
                    print(get_pgrm(node[2][i])[1] + difference)
                    exit()  # It works okay, don't judge
                i += 1
    return sum(weights) + node[1]


inspect(get_root())
