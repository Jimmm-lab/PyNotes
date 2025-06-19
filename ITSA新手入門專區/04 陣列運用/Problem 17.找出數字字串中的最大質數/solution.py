N = input()

def isPrime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def getMaxPrime(N):
    for i in range(len(N), 0, -1):
        for j in range(0, len(N)-i+1):
            s = ''
            for k in range(0, i):
                s += N[k+j]
            if isPrime(int(s)):
                return s
    return "No prime found"

print(getMaxPrime(N))
