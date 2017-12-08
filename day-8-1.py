instructions = []
while True:
    line = input()
    if line == "":
        break
    parts = line.split()[:]
    register = parts[0]
    cmd = parts[1]
    val = int(parts[2])
    condition = parts[4:]
    instructions.append([register, cmd, val, condition])

registers = {}

for instruction in instructions:
    if instruction[0] not in registers:
        registers[instruction[0]] = 0
    if instruction[3][0] not in registers:
        registers[instruction[3][0]] = 0
    condition = str(registers[instruction[3][0]]) + " " + instruction[3][1] + " " + instruction[3][2]
    if eval(condition):
        if instruction[1] == "inc":
            registers[instruction[0]] += instruction[2]
        else:
            registers[instruction[0]] -= instruction[2]

print(max(registers.values()))