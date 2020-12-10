from time import *
start = time()
i = 248345
result_1 = 0
result_2 = 0
while i <= 746315:
    k = 1
    flag_1 = 0
    count = [10]
    repeated_number = 1
    while k < len(str(i)):
        if str(i)[k-1] > str(i)[k]:  # we check for increasing numbers
            flag_1 = 0
            break
        elif str(i)[k-1] == str(i)[k]:  # we check for adjacent numbers
            flag_1 = 1
            repeated_number += 1
        elif repeated_number > 1 and str(i)[k-1] <= str(i)[k]:
            count.append(repeated_number)
            repeated_number = 1
        k += 1
    if repeated_number > 1:
        count.append(repeated_number)
    if flag_1:
        result_1 += 1
        if min(count) == 2:
            result_2 += 1
    i += 1
print("Secure Container: " + str(result_1))
print("Part two: " + str(result_2))
print(time() - start)
