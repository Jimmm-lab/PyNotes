n = int(input())

a = b = c = d = e = 0
while n > 0:
    g = int(input())
    if g >= 90 and g <= 100:
        a += 1
    if g >= 80 and g <= 89:
        b += 1
    if g >= 70 and g <= 79:
        c += 1
    if g >= 60 and g <= 69:
        d += 1
    if g >= 0 and g <= 59:
        e += 1
    n -= 1

print(f"優等 {a}\n甲等 {b}\n乙等 {c}\n丙等 {d}\n不及格 {e}")
