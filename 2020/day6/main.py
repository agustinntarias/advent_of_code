with open("input", "r") as file:
    questions = file.read().split('\n\n')
    group = questions[0]
    print("part a: ", end = "")
    print(sum(len(set(filter(lambda c: c != "\n", group))) for group in questions))
    # part b
    print("part b: ", end = "")
    print(sum(len(set.intersection(*[set(person) for person in group.split('\n') if person != ""])) for group in questions))
