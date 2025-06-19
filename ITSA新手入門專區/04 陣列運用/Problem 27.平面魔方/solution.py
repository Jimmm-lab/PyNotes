n, r = map(str, input().split())
n = int(n)

matrix = []
x = 1
for i in range(n):
    l = []
    for j in range(n):
        l.append(x)
        x += 1
    matrix.append(l)

def R(matrix):
    for col in range(n):
        for row in range(n-1, -1, -1):
            print(matrix[row][col], end='')
            if row > 0:
                print(' ', end='')
        print()
    '''30 20 10 00
       31 21 11 01
       32 22 12 02
       33 23 13 03'''

def L(matrix):
    for col in range(n-1, -1, -1):
        for row in range(n):
            print(matrix[row][col], end='')
            if row < n-1:
                print(' ', end='')
        print()
    '''03 13 23 33
       02 12 22 32
       01 11 21 31
       00 10 20 30'''

def F(matrix):
    for row in range(n-1, -1, -1):
        for col in range(n):
            print(matrix[row][col], end='')
            if col < n-1:
                print(' ', end='')
        print()
    '''30 31 32 33
       20 21 22 23
       10 11 12 13
       00 01 02 03'''

Rotate = {
    "L": L,
    "R": R,
    "F": F
}
Rotate[r](matrix)
