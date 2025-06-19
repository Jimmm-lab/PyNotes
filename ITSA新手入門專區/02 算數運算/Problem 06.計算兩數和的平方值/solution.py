n = int(input())

while n > 0:
    x, y = map(int, input().split())
    z = x+y
    print(z*z)
    n -= 1
