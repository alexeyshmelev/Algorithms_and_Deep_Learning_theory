n = int(input())
coord = []
for _ in range(n):
    coord.append(tuple(map(int, input().split())))
coord.sort(key=lambda tup: (tup[0], tup[1]))
ans = 0
for i in range(len(coord)-1):
    if coord[i][0] != coord[i+1][0]:
        ans += 1
ans += 1
print(ans)

