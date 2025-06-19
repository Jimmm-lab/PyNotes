n = int(input())

while n > 0:
    x = int(input())
    if x > 50 and x <= 70:
        y = x
    else:
        y = 100
    print(y)
    n -= 1
