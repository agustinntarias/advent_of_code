with open("input", "r") as file:
    area = file.read().strip().split('\n')
    slopes_a = [
        (3, 1)
    ]
    slopes_b = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    result = 1
    for b, a in slopes_b:
        count = x = y = 0
        while x < len(area):
            if area[x][y] == '#': count += 1
            x += a; y += b - len(area[0]) if y + b >= len(area[0]) else b

        result *= count
    print(result)
