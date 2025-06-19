a, b, c = map(int, input().split())

max = a
if b > max:
    max = b
if(c > max):
    max = c
print(max)
