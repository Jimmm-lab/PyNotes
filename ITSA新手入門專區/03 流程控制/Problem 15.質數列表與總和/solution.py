k = int(input())

def isPrime(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

i = 2
sum = 0
while k > 0:
    if isPrime(i):
        sum += i
        print(i, end='')
        if k > 1:
            print(',', end='')
        k -= 1
    i +=1
print('\n', sum, sep='')
