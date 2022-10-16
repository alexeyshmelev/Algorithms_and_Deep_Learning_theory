params = {'freeze': 'mmin',
          'heat': 'mmax',
          'auto': 'mlast',
          'fan': 'mfirst'}


def mlast(x, d):
    return x[-1]


def mfirst(x, d):
    return x[0]


def mmin(x, d):
    if d > 0:
        return x[0]
    else:
        return x[1]


def mmax(x, d):
    if d > 0:
        return x[1]
    else:
        return x[0]

try:
    f = open('input.txt')
    lines = f.readlines()
    f.close()
except FileNotFoundError:
    lines = []
    lines.append(input())
    lines.append(input())

if lines[0].split(' ')[0].lstrip('-').isdigit() and lines[0].split(' ')[1][:-1].lstrip('-').isdigit() and ''.join(lines[1].split('\n')) in params.keys():
    ts, param = list(map(int, lines[0].split(' '))), ''.join(lines[1].split('\n'))

    if -50 <= ts[0] <= 50 and -50 <= ts[1] <= 50:
        print(locals()[params[param]](ts, ts[1]-ts[0]))
    else:
        print('Temperature error!')
else:
    print('Wrong input!')