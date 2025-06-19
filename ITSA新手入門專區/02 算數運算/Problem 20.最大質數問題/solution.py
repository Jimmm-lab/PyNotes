N = int(input())

def isPrime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return False
    return True

for i in range(N-1, 0, -1):
    if isPrime(i):
        print(i)
        break
