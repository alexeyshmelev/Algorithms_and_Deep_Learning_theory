n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
ind_2 = 0
count = 0
total = nums[0]
for i in range(n):
    ind_1 = i
    while ind_2 < n-1:
        if total == k:
            count += 1
            total -= nums[ind_1]
            break
        elif total + nums[ind_2+1] <= k:
            total += nums[ind_2+1]
            ind_2 += 1
        else:
            total -= nums[ind_1]
            break
if total == k:
    print(count+1)
else:
    print(count)

