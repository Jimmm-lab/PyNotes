n = int(input())

MAX = int(input())
while n > 1:
    x = int(input())
    if x > MAX:
        MAX = x
    n -= 1
print(MAX)
