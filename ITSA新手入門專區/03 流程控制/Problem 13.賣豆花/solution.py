S = int(input())

print('百元', S//100)
S %= 100

print('十元', S//10)
S %= 10

print('壹元', S)
