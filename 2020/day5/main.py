string = "BBFFBBFRLL"
part_a = False
def getRowOrCol(string, left, right, takeLowerHalf):
    for half in string:
        if half == takeLowerHalf:
            right = (left+right-1)//2
        else:
            left = (left+right-1)//2 + 1
    return left

if part_a: maxID = 0
IDS = [0]*(127+1)*(8+1)
minId = 1000
with open("input", "r") as file:
    for boardingPass in file.readlines():
        boardingPass = boardingPass.strip('\n')
        row, column = getRowOrCol(boardingPass[:-3], 0, 127, 'F'), getRowOrCol(boardingPass[-3:], 0, 7, 'L')
        ID = row * 8 + column
        if part_a:
            if ID > maxID:
                maxID = ID
        else:
            IDS[ID] = 1
            if ID < minId:
                minId = ID


if part_a:
    print(maxID)
else:
    i = minId
    while i < len(IDS) - 2:
        if IDS[i + 1] == 0 and IDS[i + 2] == 1:
            pass
            print(i+1)
        i += 1
