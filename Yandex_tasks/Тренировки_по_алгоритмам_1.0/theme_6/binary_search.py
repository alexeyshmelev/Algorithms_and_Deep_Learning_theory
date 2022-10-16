def binary_search(lst, num, count):
    l = 0
    r = count - 1
    while l < r:
        m = (l + r) // 2
        if num <= lst[m]:
            r = m
        else:
            l = m + 1
    if num == lst[l]:
        print("YES")
    else:
        print("NO")


n, k = list(map(int, input().split()))
list_1 = list(map(int, input().split()))
list_2 = list(map(int, input().split()))
for elem in list_2:
    binary_search(list_1, elem, n)

