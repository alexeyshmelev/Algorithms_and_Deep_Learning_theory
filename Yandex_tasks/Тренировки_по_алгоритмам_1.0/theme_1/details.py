n, k, m = list(map(int, input().split()))

mass = n
det = 0
if k >= m:
    while mass >= k:
        det += (mass // k)*(k // m)
        mass = mass % k + (mass // k)*(k % m)
print(det)

