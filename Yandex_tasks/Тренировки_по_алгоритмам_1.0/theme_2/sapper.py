n, m, k = list(map(int, input().split()))
points = []
for _ in range(k):
    points.append(tuple(map(int, input().split())))

dx = (-1, -1, -1, 0, 0, 1, 1, 1)
dy = (-1, 0, 1, -1, 1, -1, 0, 1)

field = []
for _ in range(n+2):
    field.append([0]*(m+2))

for x, y in points:
    for i in range(8):
        field[x+dx[i]][y+dy[i]] += 1

for x, y in points:
    field[x][y] = "*"

for i in range(1, n+1):
    for j in range(1, m+1):
        print(field[i][j], end=" ")
    print()

