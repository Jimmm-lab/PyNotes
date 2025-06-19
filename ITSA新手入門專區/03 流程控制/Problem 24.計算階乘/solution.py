n = int(input())

while n > 0:
    x = int(input())
    sum = 1
    for i in range(2, x+1):
        sum *= i
    print(sum)
    n -= 1
