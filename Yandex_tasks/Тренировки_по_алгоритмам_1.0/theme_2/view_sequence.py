const = 1
ascend = 1
weak_ascend = 1
descend = 1
weak_descend = 1
count = 0

num = int(input())

while num != -2*10**9:
    count += 1
    num_new = int(input())
    if num_new != -2*10**9:
        if num_new == num:
            const += 1
        if num_new > num:
            ascend += 1
        if num_new >= num:
            weak_ascend += 1
        if num_new < num:
            descend += 1
        if num_new <= num:
            weak_descend += 1
    num = num_new

if count == const:
    print("CONSTANT")
elif count == ascend:
    print("ASCENDING")
elif count == weak_ascend:
    print("WEAKLY ASCENDING")
elif count == descend:
    print("DESCENDING")
elif count == weak_descend:
    print("WEAKLY DESCENDING")
else:
    print("RANDOM")

