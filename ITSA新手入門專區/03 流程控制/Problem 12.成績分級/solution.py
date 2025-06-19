n = int(input())

while n > 0:
    x = int(input())
    if x >= 0 and x <= 59:
        print('不及格')
    elif x >= 60 and x <= 69:
        print('丙等')
    elif x >= 70 and x <= 79:
        print('乙等')
    elif x >= 80 and x <= 89:
        print('甲等')
    elif x >= 90 and x <= 100:
        print('優等')
    n -= 1
