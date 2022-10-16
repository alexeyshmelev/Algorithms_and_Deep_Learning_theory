troom, tcond = list(map(int, input().split()))
command = input()

if command == "freeze":
    if troom > tcond:
        print(tcond)
    else:
        print(troom)

if command == "heat":
    if troom < tcond:
        print(tcond)
    else:
        print(troom)

if command == "auto":
    print(tcond)

if command == "fan":
    print(troom)

