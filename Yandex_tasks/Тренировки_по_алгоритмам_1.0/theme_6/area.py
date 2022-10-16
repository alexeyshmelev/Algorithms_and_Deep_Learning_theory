def binary_search(n, m, t):
    l = 0
    r = max(n, m) // 2
    while l < r:
        s = (l + r + 1) // 2
        if 4*s**2 + s*(n - 2*s)*2 + s*(m - 2*s)*2 <= t:
            l = s
        else:
            r = s - 1
    print(l)


n = int(input())
m = int(input())
t = int(input())
binary_search(n, m, t)

