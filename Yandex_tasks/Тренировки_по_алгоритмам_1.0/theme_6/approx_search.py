def binary_search(lst, num, count):
    l = 0
    r = count - 1
    while l < r:
        m = (l + r) // 2
        if num <= lst[m]:
            r = m
        else:
            l = m + 1
    if l > 0:
        if abs(lst[l] - num) < abs(lst[l-1] - num):
            print(lst[l])
        else:
            print(lst[l-1])
    else:
        print(lst[l])


n, k = list(map(int, input().split()))
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
for elem in list_2:
    binary_search(list_1, elem, n)

