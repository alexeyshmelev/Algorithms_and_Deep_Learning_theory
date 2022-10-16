a = list(map(int, input().split()))

flag = False
for i in range(len(a)-1):
    if a[i+1] - a[i] <= 0:
        flag = True
        break
if flag:
    print("NO")
else:
    print("YES")

