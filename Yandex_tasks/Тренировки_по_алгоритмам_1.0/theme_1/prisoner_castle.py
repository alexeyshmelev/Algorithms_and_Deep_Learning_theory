def sort(x, y):
    if x < y:
        return (x, y)
    else:
        return (y, x)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

a, b = sort(a, b)
b, c = sort(b, c)
a, b = sort(a, b)
d, e = sort(d, e)

if a <= d and b <= e:
    print("YES")
else:
    print("NO")

