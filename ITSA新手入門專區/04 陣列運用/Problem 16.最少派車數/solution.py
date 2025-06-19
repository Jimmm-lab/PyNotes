n = int(input())

i = 0
s = []
d = []
while i < n:
    a, b = map(int, input().split())
    s.append(a)
    d.append(b)
    i += 1

for i in range(0, len(d)):
    for j in range(i+1, len(s)):
        if d[i] == s[j]:
            n -= 1

print(n)
