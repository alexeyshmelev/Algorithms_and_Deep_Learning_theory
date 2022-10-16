n = int(input())
list_cliks = list(map(int, input().split()))
buttons = {}
for i in range(n):
    buttons[i+1] = list_cliks[i]
m = int(input())
seq = list(map(int, input().split()))
now_buttons = {}
for i in range(n):
    now_buttons[i+1] = 0
for elem in seq:
    now_buttons[elem] += 1
for i in range(n):
    if now_buttons[i+1] - buttons[i+1] > 0:
        print('YES')
    else:
        print('NO')

