N, M = map(str, input().split())

count = 0
for i in range(len(M)-len(N)+1):
    flag = False
    for j in range(0, len(N)):
        if N[j] == M[j+i]:
            flag = True
        else:
            flag = False
            break
    if flag:
        count += 1

print(count)
