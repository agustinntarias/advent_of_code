import re
FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
validPassports = 0
with open("input", "r") as file:
    passports = file.read().split('\n\n')
    for passport in passports:

        # part a
        # presentFields = all(passport.count(field) == 1 for field in FIELDS)
        # if presentFields:
        #     validPassports += 1

        # part b
        regex = (
            r"(?sm)"  # multiline search
            r"(?=.*byr:(19[2-9]\d|200[0-2]))?"  # 1920 <= byr <= 2002
            r"(?=.*iyr:(201\d|2020))?"  # 2010 <= iyr <= 2020
            r"(?=.*eyr:(202\d|2030))?"  # 2020 <= eyr <= 2030
            r"(?=.*hgt:(1[5-8]\dcm|19[0-3]cm|6\din|59in|7[0-6]in))?"  # 150cm <= hgt <= 193cm or 59in <= hgt <= 76in
            r"(?=.*hcl:#([0-9a-f]*))?"  # hcl = #(six digits or a-f)
            r"(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))?"  # ecl only one of determined values
            r"(?=.*pid:(\d{9})\b)?")  # pid of 9 digits
        if all(field != None for field in re.match(regex, passport).groups()):
            validPassports += 1


print(validPassports)
