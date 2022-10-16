n = int(input())
seq = list(map(int, input().split()))
num = int(input())

ans = seq[0]
for member in seq:
    if abs(member - num) - abs(ans - num) < 0:
        ans = member
print(ans)

