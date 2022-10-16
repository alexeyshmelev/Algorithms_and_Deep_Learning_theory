file = open('input.txt')
words = []
for line in file.readlines():
    words += line.split()
file.close()
vcb = {}
for word in words:
    if not (word in vcb.keys()):
        vcb[word] = 1
    else:
        vcb[word] += 1
vcb = dict(sorted(vcb.items()))
max_count = 0
ans = ''
for elem in vcb.keys():
    if max_count < vcb[elem]:
        max_count = vcb[elem]
        ans = elem
print(ans)

