n = int(input())

N = n
a = b = 0
total = 0
MAX = 0
while N > 0:
    g = int(input())
    if g > MAX:
        MAX = g
    if g >= 900:
        a += 1
    if g > 600 and g <= 700:
        b += 1
    total += g
    N -= 1
avg = "{:.1f}".format(round(total/n, 1))

print(MAX, a, b, avg, sep='\n')
