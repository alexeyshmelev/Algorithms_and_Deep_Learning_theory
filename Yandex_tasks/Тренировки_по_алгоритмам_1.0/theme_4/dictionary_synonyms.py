n = int(input())
vcb = {}
for _ in range(n):
    k, v = input().split()
    vcb[k] = v
word = input()
for elem in vcb.keys():
    if elem == word or vcb[elem] == word:
        if elem == word:
            print(vcb[elem])
            break
        else:
            print(elem)
            break

