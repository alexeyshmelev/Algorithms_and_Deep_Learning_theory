a = int(input())
b = int(input())
n = int(input())
m = int(input())

min_1 = a*(n-1) + n
min_2 = b*(m-1) + m
max_1 = a*(n+1) + n
max_2 = b*(m+1) + m

min_0 = max(min_1, min_2)
max_0 = min(max_1, max_2)

if max_0 >= min_0:
    print(min_0, max_0)
else:
    print(-1)

