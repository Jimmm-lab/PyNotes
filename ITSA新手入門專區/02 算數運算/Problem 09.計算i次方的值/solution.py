n = int(input())

while n > 0:
    i = int(input())
    if i > 31:
        print('Value of more than 31')
    else:
        print(2 << i-1)
    n -= 1
