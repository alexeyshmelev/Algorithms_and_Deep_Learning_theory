lines = []
lines.append(input())
lines.append(input())
lines.append(input())

if all([char.split('\n')[0].isdigit() for char in lines]):
    lines = [int(char.split('\n')[0]) for char in lines]
    for i in range(2):
        for j in range(i+1, 3):
            try:
                if lines[i] + lines[j] <= [lines[k] for k, _ in enumerate(lines) if k!=i and k!=j and lines[k]>0][0]:
                    print('NO')
                    break
            except:
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')
else:
    print('NO')
