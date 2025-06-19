d = int(input())

Hex = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

s = ''
while d != 0:
    if d % 16 >= 10:
        s += Hex[d % 16]
    else:
        s += str(d % 16)
    d //= 16
print(s[::-1])
