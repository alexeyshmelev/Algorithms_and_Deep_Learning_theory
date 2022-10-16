def binary_search(w, h, n):
    l = 0
    r = max(w, h)*n
    while l < r:
        m = (l + r) // 2
        if (m // w) * (m // h) >= n:
            r = m
        else:
            l = m + 1
    print(l)


w, h, n = list(map(int, input().split()))
binary_search(w, h, n)

