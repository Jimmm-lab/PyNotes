l = list(map(int, input().split()))
d = input()

if d == "Asc":
    l.sort()
    i = 0
    for num in l:
        print(num, end='')
        if i < len(l)-1:
            print('<', end='')
            i += 1
    print()
if d == "Desc":
    l.sort(reverse=True)
    i = 0
    for num in l:
        print(num, end='')
        if i < len(l)-1:
            print('>', end='')
            i += 1
    print()
