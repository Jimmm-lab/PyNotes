Y = int(input())

if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0:
    print('Bissextile Year')
else:
    print('Common Year')
