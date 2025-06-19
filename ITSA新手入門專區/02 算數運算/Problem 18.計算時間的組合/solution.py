N = int(input())

d = N // 86400
N %= 86400
print(d, 'days')

h = N // 3600
N %= 3600
print(h, 'hours')

m = N // 60
N %= 60
print(m, 'minutes')

s = N
print(s, 'seconds')
