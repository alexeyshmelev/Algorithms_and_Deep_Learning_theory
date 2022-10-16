seq = list(map(int, input().split()))

ans = 0
for i in range(1,len(seq)-1):
    if seq[i] - seq[i-1] > 0 and seq[i] - seq[i+1] > 0:
        ans += 1
print(ans)

