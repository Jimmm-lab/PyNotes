M, N = map(int, input().split())

while N != 0:
    R = M % N
    M = N
    N = R

print(M)
