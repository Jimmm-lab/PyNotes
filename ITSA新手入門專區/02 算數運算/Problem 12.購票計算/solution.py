N = int(input())

a = N // 10
N %= 10
print('NT10=', a, sep='')

b = N // 5
N %= 5
print('NT5=', b, sep='')

c = N
print('NT1=', c, sep='')
