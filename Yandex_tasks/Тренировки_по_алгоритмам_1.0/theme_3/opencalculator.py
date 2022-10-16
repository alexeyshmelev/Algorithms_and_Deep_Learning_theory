buttons = set(map(int, input().split()))
num = set(map(int, input()))
ans = 0
for elem in num:
    if not (elem in buttons):
        ans += 1
print(ans)

