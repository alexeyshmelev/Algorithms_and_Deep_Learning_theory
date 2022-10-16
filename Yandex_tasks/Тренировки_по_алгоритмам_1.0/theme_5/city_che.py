n, r = list(map(int, input().split()))
distance = list(map(int, input().split()))
ind_1 = 0
ind_2 = 0
count = 0
while ind_1 < n:
    while ind_2 < n and distance[ind_2] - distance[ind_1] <= r:
        ind_2 += 1
    count += n - ind_2
    ind_1 += 1
print(count)

