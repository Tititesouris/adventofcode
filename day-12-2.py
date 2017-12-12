instructions = {}
while True:
    line = input()
    if line == "":
        break
    parts = line.split(" <-> ")
    source = int(parts[0])
    dests = list(map(int, parts[1].split(", ")))
    instructions[source] = dests

left = [*instructions][:]
nbGroups = 0
while left != []:
    nbGroups += 1
    visited = []
    stack = [left.pop(0)]
    while stack != []:
        programs = []
        for program in stack:
            visited.append(program)
            for dest in instructions[program]:
                if dest not in visited and dest not in stack:
                    programs.append(dest)
                    left.remove(dest)
        stack = programs[:]
print(nbGroups)
