s = input()

for ch in s:
    for i in range(0, int(ch)):
        print('*', sep='', end='')
    print()
