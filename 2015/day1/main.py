# part a
with open("input", "r") as file: x = file.read(); print((lambda y: y.count('(')-y.count(')'))(x))

# part b
with open("input", "r") as file:
    instructions = file.read()
    position = 0
    level = 0
    INSTRUCTIONS={
        '(':1,
        ')':-1,
    }
    while level != -1:
        level+=INSTRUCTIONS[instructions[position]]
        position+=1
    print(position)
