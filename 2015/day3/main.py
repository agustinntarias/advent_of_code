with open("input", "r") as file:
    moves = file.read()
    santa = (0, 0)
    robot_santa = (0, 0)
    switch = 1
    houses = set()
    directions = {
        '^' : (0, 1),
        '>' : (1, 0),
        'v' : (0, -1),
        '<' : (-1, 0),
    }
    for move in moves:
        if switch:
            santa = (santa[0] + directions[move][0], santa[1] + directions[move][1])
            houses.add(santa)
        else:
            robot_santa = (robot_santa[0] + directions[move][0], robot_santa[1] + directions[move][1])
            houses.add(robot_santa)
        switch = 1 - switch
    print(len(houses))
