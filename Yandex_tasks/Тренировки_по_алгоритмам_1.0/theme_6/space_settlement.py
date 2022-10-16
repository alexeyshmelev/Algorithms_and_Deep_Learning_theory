def binary_search(n, a, b, w, h):
    l = 0
    r = max(w, h)
    while l < r:
        m = (l + r + 1) // 2
        if (w // (a + 2*m)) * (h // (b + 2*m)) >= n:
            l = m
        else:
            r = m - 1
    l_1 = l
    l = 0
    r = max(w, h)
    while l < r:
        m = (l + r + 1) // 2
        if (h // (a + 2 * m)) * (w // (b + 2 * m)) >= n:
            l = m
        else:
            r = m - 1
    if l > l_1:
        return print(l)
    else:
        return print(l_1)


n, a, b, w, h = list(map(int, input().split()))
binary_search(n, a, b, w, h)

