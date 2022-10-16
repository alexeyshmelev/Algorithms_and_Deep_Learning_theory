genome_1 = input()
genome_2 = input()
couples_1 = []
couples_2 = []
for i in range(len(genome_1)-1):
    couples_1.append(genome_1[i] + genome_1[i+1])
for i in range(len(genome_2)-1):
    couples_2.append(genome_2[i] + genome_2[i+1])
set_1 = set(couples_1)
set_2 = set(couples_2)
common_set = set_1 & set_2
ans = 0
for elem in common_set:
    ans += couples_1.count(elem)
print(ans)

