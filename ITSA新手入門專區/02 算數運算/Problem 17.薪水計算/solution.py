T, S = map(int, input().split())

if T <= 60:
    m = T*S
elif T > 60 and T < 121:
    m = 60*S
    T -= 60
    m += T*S*1.33
elif T > 121:
    m = 60*S*2.33
    T -= 120
    m += T*S*1.66

print(m)
