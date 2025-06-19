N = int(input())
A = list(map(int, input().split()))

B = []
for i in range(0, N):
    sum = 0
    for j in range(0, i+1):
        sum += A[j]
    B.append(sum)

for num in B:
    print(num, end='')
    if N > 1:
        print(' ', end='')
        N -= 1
print()
