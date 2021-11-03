select = input("Select operation a / b: ")
d = {}

if select == "a":
    str = input("Enter the text: ")
    for i in set(str):
        d[i] = str.count(i)

    print(d)

if select == "b":
    enter = input("Enter the text: ").split()
    y = []
    for i in sorted(enter):
        if i not in y:
            y.append(i)

print(' '.join(y))