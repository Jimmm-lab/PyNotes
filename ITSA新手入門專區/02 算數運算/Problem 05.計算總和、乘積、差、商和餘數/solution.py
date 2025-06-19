data = input()
l = data.split()
x = int(l[0])
y = int(l[1])

print(x, '+', y, '=', x+y, sep='')
print(x, '*', y, '=', x*y, sep='')
print(x, '-', y, '=', x-y, sep='')
q = x//y
r = x-q*y
if r < 0:
    q += 1
    r = x-q*y
print(x, '/', y, '=', q, '...', r, sep='')
