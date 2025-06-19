n = int(input())

while n > 0:
    X, Y = map(int, input().split())
    sum = (X+Y)*(abs(X-Y)+1)/2
    print(int(sum))
    n -= 1
