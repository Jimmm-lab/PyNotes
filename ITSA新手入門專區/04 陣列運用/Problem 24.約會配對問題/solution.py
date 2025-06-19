n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

a = []
b = []
used_boys = set()
used_girls = set()
count = 0

while count < n:
    max_val = -1
    selected_boy = -1
    selected_girl = -1

    for i in range(n):
        if i in used_boys:
            continue
        for j in range(n):
            if j in used_girls:
                continue
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                selected_boy = i
                selected_girl = j

    if selected_boy != -1 and selected_girl != -1:
        a.append(selected_boy)
        b.append(selected_girl)
        used_boys.add(selected_boy)
        used_girls.add(selected_girl)
        count += 1

for i in range(n):
    print(f"boy {a[i]+1} pair with girl {b[i]+1}")


'''N = int(input())

l = []
i = 0
while i < N:
    l.append(list(map(int, input().split())))
    i += 1

bestPath = []
MAX = [float('-INF')]
def getMaxGrade(matrix, row, usedCols, currSum, path):
    if row == len(matrix):
        if currSum > MAX[0]:
            MAX[0] = currSum
            bestPath.clear()
            bestPath.extend(path)
        return

    for col in range(len(matrix[row])):
        if col not in usedCols:
            getMaxGrade(
                matrix,
                row + 1,
                usedCols | {col},
                currSum + matrix[row][col],
                path + [(row, col)]
            )

getMaxGrade(l, 0, set(), 0, [])
bestPath.sort(reverse=True, key=lambda x: l[x[0]][x[1]])
for row, col in bestPath:
    print(f"boy {row+1} pair with girl {col+1}")'''
