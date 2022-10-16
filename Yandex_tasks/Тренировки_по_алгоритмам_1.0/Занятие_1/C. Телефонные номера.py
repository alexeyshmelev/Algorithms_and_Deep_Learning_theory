phones = []
phones.append(input())
phones.append(input())
phones.append(input())
phones.append(input())

dict = {ord('-'): None,
       ord('('): None,
       ord(')'): None,
       ord(' '): None,
       ord('+'): None}

for i in range(len(phones)):
    phones[i] = phones[i].translate(dict)
    if len(phones[i]) == 11:
        phones[i] = [phones[i][1:4], phones[i][4:]]
    elif len(phones[i]) == 7:
        phones[i] = ['495', phones[i]]
    else:
        phones[i] = [None, None]

for i in range(1, len(phones)):
    if phones[0][0] == phones[i][0] and phones[0][1] == phones[i][1]:
        print('YES')
    else:
        print('NO')