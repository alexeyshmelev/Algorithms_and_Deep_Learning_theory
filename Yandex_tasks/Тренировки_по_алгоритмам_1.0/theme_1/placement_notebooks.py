a_1, b_1, a_2, b_2 = list(map(int, input().split()))

a = b_1 + b_2
b = max(a_1, a_2)
s = a*b

if (a_1 + b_2)*max(b_1, a_2) < s:
    a = a_1 + b_2
    b = max(b_1, a_2)
    s = a*b
if (a_1 + a_2)*max(b_1, b_2) < s:
    a = a_1 + a_2
    b = max(b_1, b_2)
    s = a*b
if (a_2 + b_1)*max(a_1, b_2) < s:
    a = a_2 + b_1
    b = max(a_1, b_2)
print(a, b)

