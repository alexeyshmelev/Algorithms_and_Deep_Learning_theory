file = open('input.txt')
users = {}
for line in file.readlines():
    name, product, count = line.split()
    count = int(count)
    if not (name in users.keys()):
        users[name] = {product: count}
    else:
        if not (product in users[name].keys()):
            users[name][product] = count
        else:
            users[name][product] += count
file.close()
users = dict(sorted(users.items()))
for person, items in users.items():
    print(person + ":")
    items = dict(sorted(items.items()))
    for item, count in items.items():
        print(item, count)

