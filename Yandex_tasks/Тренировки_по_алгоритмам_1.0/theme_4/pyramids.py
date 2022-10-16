n = int(input())
blocks = {}
for _ in range(n):
    w, h = list(map(int, input().split()))
    if w in blocks.keys():
        if h > blocks[w]:
            blocks[w] = h
    else:
        blocks[w] = h
ans = 0
for elem in blocks.values():
    ans += elem
print(ans)

