a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")
elif c == 0:
    if a == 0:
        if b == 0:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")
    else:
        ans = -b / a
        if ans - int(ans) == 0:
            print(int(ans))
        else:
            print("NO SOLUTION")
else:
    if a == 0:
        if b >= 0 and b == c**2:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")
    else:
        ans = (c**2 - b)/a
        if ans - int(ans) == 0:
            print(int(ans))
        else:
            print("NO SOLUTION")

