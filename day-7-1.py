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


print(get_root()[0])
