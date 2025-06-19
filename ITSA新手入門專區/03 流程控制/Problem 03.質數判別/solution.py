N = int(input())

def isPrime(N):
    if N <= 1:
        return "NO"
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return "NO"
    return "YES"

print(isPrime(N))
