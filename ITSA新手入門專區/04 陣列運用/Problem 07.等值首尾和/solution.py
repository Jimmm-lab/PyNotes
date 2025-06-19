n = int(input())
A = list(map(int, input().split()))

count = 0
PS = 0
for i in range(0, n):
    PS += A[i]
    for j in range(1, n+1):
        SS = 0
        for k in range(n-1, n-j-1, -1):
            SS += A[k]
        if SS == PS:
            count += 1
print(count)
