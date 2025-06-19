R, C = map(int, input().split())

matrix = []
for _ in range(R):
    matrix.append(list(map(int, input().split())))

for i in range(C):
    for j in range(R):
        print(matrix[j][i], end='')
        if j < R-1:
            print(' ', end='')
    print()
