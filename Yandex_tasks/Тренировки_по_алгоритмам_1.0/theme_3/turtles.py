n = int(input())
ans = set()
for _ in range(n):
    a, b = map(int, input().split())
    if a >= 0 and b >= 0 and a + b == n-1 and not (a in ans):
        ans.add(a)
print(len(ans))

