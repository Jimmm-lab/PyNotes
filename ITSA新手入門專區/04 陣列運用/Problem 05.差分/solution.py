N = int(input())
A = list(map(int, input().split()))

B = [A[0]]
for i in range(1, N):
    diff = A[i]-A[i-1]
    B.append(diff)

for diff in B:
    print(diff, end='')
    if N > 1:
        print(' ', end='')
        N -= 1
print()
