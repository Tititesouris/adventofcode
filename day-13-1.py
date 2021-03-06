layers = {}
while True:
    line = input()
    if line == "":
        break
    parts = line.split(": ")
    layer = int(parts[0])
    depth = int(parts[1])
    layers[layer] = depth

firewall = []
for i in range(max(layers.keys()) + 1):
    if i in layers:
        firewall.append([0 for _ in range(layers[i])])
        firewall[i][0] = 1
    else:
        firewall.append([])

severity = 0
for i in range(len(firewall)):
    if firewall[i] != []:
        if i % (2 * len(firewall[i]) - 2) == 0:
            severity += i * len(firewall[i])
print(severity)