n = int(input())
students = []
for _ in range(n):
    now_set = set()
    m = int(input())
    for _ in range(m):
        now_set.add(input())
    students.append(now_set)
common_set = set(students[0])
for elem in students:
    common_set &= elem
print(len(common_set))
for elem in common_set:
    print(elem)
another_set = students[0]
for elem in students:
    another_set = another_set.union(elem)
print(len(another_set))
for elem in another_set:
    print(elem)

