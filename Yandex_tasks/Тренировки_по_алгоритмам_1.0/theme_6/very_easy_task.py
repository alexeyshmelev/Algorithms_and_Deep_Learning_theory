def binary_search(N, x, y):
    l = 0
    r = max(x, y)*N
    while l < r:
        m = (l + r) // 2
        if m // x + m // y >= N - 1:
            r = m
        else:
            l = m + 1
    print(l + min(x, y))


N, x, y = list(map(int, input().split()))
binary_search(N, x, y)

