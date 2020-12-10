import re
validPwds = 0
with open("input", "r") as file:
    for line in file.readlines():
        regex = r"(\d*)\-(\d*)\ (\w): (\w*)"
        m = re.match(regex, line)

        # part a
        # lowerBound, upperBound, letter, string = m.groups()
        # numberOcurrences = string.count(letter)
        # if numberOcurrences <= int(upperBound) and numberOcurrences >= int(lowerBound):
        #     validPwds+=1

        #part b
        firstIndx, secondIndx, letter, string = m.groups()
        firstIndx, secondIndx = int(firstIndx)-1, int(secondIndx)-1
        firstIndxBoolean = (string[firstIndx] == letter) if firstIndx < len(string) else False
        secondIndxBoolean = (string[secondIndx] == letter) if secondIndx < len(string) else False

        if  firstIndxBoolean + secondIndxBoolean == 1:
            validPwds+=1


print(validPwds)
