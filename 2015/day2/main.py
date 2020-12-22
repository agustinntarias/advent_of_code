with open("input", "r") as file:
    x = file.read()
    print(sum((lambda a,b,c: 2*a*b+2*a*c+2*b*c+a*b)(*sorted(list(map(int, line.split('x'))))) for line in x.split('\n') if line != ''))
    print(sum((lambda a,b,c: 2*(a+b)+a*b*c)(*sorted(list(map(int, line.split('x'))))) for line in x.split('\n') if line != ''))



