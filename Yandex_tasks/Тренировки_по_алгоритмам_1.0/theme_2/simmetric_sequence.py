def remains_palindrome(seq):
    for point in range(len(seq)):
        i = point
        j = len(seq) - 1
        while j >= i and seq[i] == seq[j]:
            j -= 1
            i += 1
        if i > j:
            ans = []
            for k in range(point-1, -1, -1):
                ans.append(seq[k])
            return ans


n = int(input())
seq = list(map(int, input().split()))
ans = remains_palindrome(seq)
print(len(ans))
print(*ans)

