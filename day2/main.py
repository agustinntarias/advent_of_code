with open("input.txt", "r") as file:
    program = [int(line) for line in file.read().split(",")]
    program[1] = 12
    program[2] = 2
    i = 0
    while True:
        if program[i] == 1:
            program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
        elif program[i] == 2:
            program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
        else:
            break
        i += 4
print("1202 Program Alarm: " + str(program[0]))


result = 0
file = open("input.txt", "r")
program = [int(line) for line in file.read().split(",")]
flag1 = 0
for noun in range(100):
    for verb in range(100):
        program[1] = noun
        program[2] = verb
        flag2 = 1
        i = 0
        while flag2:
            if program[i] == 1:
                program[program[i + 3]] = program[program[i + 1]] + program[program[i + 2]]
            elif program[i] == 2:
                program[program[i + 3]] = program[program[i + 1]] * program[program[i + 2]]
            else:
                flag2 = 0
            i += 4
        if program[0] == 19690720:
            flag1 = 1
            result = 100*noun + verb
            break
        file.seek(0)
        program = [int(line) for line in file.read().split(",")]
    if flag1:
        break
print("Part two: " + str(result))

