instructions = {}
while True:
    line = input()
    if line == "":
        break
    parts = line.split(" <-> ")
    source = int(parts[0])
    dests = list(map(int, parts[1].split(", ")))
    instructions[source] = dests

visited = []
stack = [0]
while stack != []:
    programs = []
    for program in stack:
        visited.append(program)
        for dest in instructions[program]:
            if dest not in visited and dest not in stack:
                programs.append(dest)
    stack = programs[:]
nbPrograms = len(visited)
print(nbPrograms)