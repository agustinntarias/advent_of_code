with open("input.txt", "r") as file:
    lis = [line.split(",") for line in file.read().split("\n")]
    wire_1 = lis[1]
    wire_2 = lis[0]
    wire_1_history = [(0, 0, 0)]
    manhattan_distances = []
    steps = []
    x = (0, 0, 0)  # x, y, steps
    for direction in wire_1:
        if direction[0] == 'R':
            x = (x[0] + int(direction[1:]), x[1], x[2] + int(direction[1:]))
            wire_1_history.append(x)
        elif direction[0] == 'L':
            x = (x[0] - int(direction[1:]), x[1], x[2] + int(direction[1:]))
            wire_1_history.append(x)
        elif direction[0] == 'U':
            x = (x[0], x[1]+int(direction[1:]), x[2] + int(direction[1:]))
            wire_1_history.append(x)
        else:
            x = (x[0], x[1] - int(direction[1:]), x[2] + int(direction[1:]))
            wire_1_history.append(x)
    wire_2_history = [(0, 0, 0)]
    x = (0, 0, 0)
    for direction in wire_2:
        if direction[0] == 'R':
            x = (x[0] + int(direction[1:]), x[1], x[2] + int(direction[1:]))
            wire_2_history.append(x)
        elif direction[0] == 'L':
            x = (x[0] - int(direction[1:]), x[1], x[2] + int(direction[1:]))
            wire_2_history.append(x)
        elif direction[0] == 'U':
            x = (x[0], x[1]+int(direction[1:]), x[2] + int(direction[1:]))
            wire_2_history.append(x)
        else:
            x = (x[0], x[1] - int(direction[1:]), x[2] + int(direction[1:]))
            wire_2_history.append(x)
        x0, y0, s0 = wire_2_history[0][0], wire_2_history[0][1], wire_2_history[0][2]
        x1, y1, s1 = wire_2_history[1][0], wire_2_history[1][1], wire_2_history[1][2]
        i = 0
        while i < len(wire_1_history)-1:
            a0, b0, p0 = wire_1_history[i][0], wire_1_history[i][1], wire_1_history[i][2]
            a1, b1, p1 = wire_1_history[i+1][0], wire_1_history[i+1][1], wire_1_history[i+1][2]
            if x0 == x1 and b0 == b1 and min(a0, a1) < x0 < max(a0, a1) and min(y0, y1) < b0 < max(y0, y1):
                manhattan_distances.append(abs(x0)+abs(b0))
                steps.append((s0 + abs(y0-b0)) + (p0 + abs(x0-a0)))
            elif y0 == y1 and a0 == a1 and min(x0, x1) < a0 < max(x0, x1) and min(b0, b1) < y0 < max(b0, b1):
                manhattan_distances.append(abs(y0) + abs(a0))
                steps.append((s0 + abs(a0 - x0)) + (p0 + abs(b0 - y0)))
            i += 1
        del wire_2_history[0]
print("Crossed wires: " + str(min(manhattan_distances)))
print("Fewest combined steps: " + str(min(steps)))
