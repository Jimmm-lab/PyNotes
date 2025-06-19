n = int(input())

while n > 0:
    BMI = float(input())
    if BMI < 18.5:
        print('體重過輕')
    elif BMI >= 18.5 and BMI < 24:
        print('正常')
    elif BMI >= 24 and BMI < 28:
        print('體重過重')
    elif BMI >= 28:
        print('肥胖')
    n -= 1
