string = "1002,4,3,4,33"
program = [int(num) for num in string.split(',')]

x, i = str(program[0]), 0
print("Program starting with initial state:\n " + string)
while x!= 99:
    if x[-1] == '1':
        # print(1, program[i+1:i+4])
        add1, add2, atAddress = program[i+1:i+4]
        program[atAddress] = program[add1] + program[add2]
        i+=4
    elif x[-1] == '2':
        prod1, prod2, atAddress = program[i+1:i+4]
        program[atAddress] = program[prod1] * program[prod2]
        i+=4
    if x[-1] == '3':
        y = program[i+1]
        n = int(input(f"Enter a number to input into address {y}: "))
        program[y] = n
        i+=2
    elif x[-1] == '4':
        y = program[i+1]
        print(f"The value at address {y} is {program[y]}")
        i+=2
    # print("Program state:\n ", program)

    x = program[i]
print("Program has halted. The final state is:\n " + ",".join(map(str,program)))
