def check(voc, val):
    if len(voc) != val:
        return False
    return True


n, k = list(map(int, input().split()))
trees = list(map(int, input().split()))

saves = {trees[0]: 1}
ind_1 = 0
ind_2 = 0
min_sigment = n
min_ind_1 = 0
min_ind_2 = n-1
while ind_1 < n:
    flag = False
    while ind_2 < n:
        if check(saves, k):
            flag = True
            break
        if ind_2 == n-1:
            break
        ind_2 += 1
        if trees[ind_2] not in saves:
            saves[trees[ind_2]] = 0
        saves[trees[ind_2]] += 1
    if ind_2 - ind_1 + 1 < min_sigment and flag:
        min_ind_1 = ind_1
        min_ind_2 = ind_2
        min_sigment = ind_2 - ind_1 + 1
    if saves[trees[ind_1]] != 1:
        saves[trees[ind_1]] -= 1
    else:
        del saves[trees[ind_1]]
    ind_1 += 1

print(min_ind_1+1, min_ind_2+1)

