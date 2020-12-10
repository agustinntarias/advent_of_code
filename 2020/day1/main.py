file = open("input", "r")
numbers = [int(line.strip('\n')) for line in file.readlines()]

indxNum1 = 0
for num1 in numbers:
    indxNum2 = 0
    for num2 in numbers[indxNum1+1:]:
        for num3 in numbers[indxNum2+1:]:
            if num1+num2+num3==2020:
                print(num1*num2*num3)
        indxNum2+=1
    indxNum1+=1



