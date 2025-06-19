m = int(input())

if m <= 800:
    m *= .9
elif m > 800 and m <1500:
    m *= .81
else:
    m *= .9*.79

print(round(m, 1))
