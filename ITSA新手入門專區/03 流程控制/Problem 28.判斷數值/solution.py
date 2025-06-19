N = int(input())

def isPrime(N):
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            return ''
    return " prime"

if N % 2:
    print(f"odd{isPrime(N)}")
else:
    print(f"even{isPrime(N)}")
