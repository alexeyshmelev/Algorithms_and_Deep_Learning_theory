import math
file = open('input.txt')

database = {}
for line in file.readlines():
    command = line.split()
    name = command[0]
    if name == 'DEPOSIT':
        person = command[1]
        count = int(command[2])
        if not (person in database.keys()):
            database[person] = 0
        database[person] += count
    elif name == 'WITHDRAW':
        person = command[1]
        count = int(command[2])
        if not (person in database.keys()):
            database[person] = 0
        database[person] -= count
    elif name == 'TRANSFER':
        person_1 = command[1]
        person_2 = command[2]
        count = int(command[3])
        if not (person_1 in database.keys()):
            database[person_1] = 0
        if not (person_2 in database.keys()):
            database[person_2] = 0
        database[person_1] -= count
        database[person_2] += count
    elif name == 'INCOME':
        p = float(command[1])
        for user in database.keys():
            if database[user] > 0:
                database[user] += p/100*database[user]
                database[user] = math.floor(database[user])
    elif name == 'BALANCE':
        person = command[1]
        if person in database.keys():
            print(database[person])
        else:
            print('ERROR')

