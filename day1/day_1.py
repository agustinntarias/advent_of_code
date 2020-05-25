puzzle_1 = 0
puzzle_2 = 0
with open("input.txt", "r") as file:
    for line in file.readlines():
        fuel = int(line.strip("\n"))
        puzzle_1 += fuel//3 - 2
        while fuel//3 - 2 > 0:
            fuel = fuel // 3 - 2
            puzzle_2 += fuel
print("Puzzle 1: " + str(puzzle_1))
print("Puzzle 2: " + str(puzzle_2))
