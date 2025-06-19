n = int(input())
p = input()
T = int(input())

j = 0
for i in range(0, (n+T-1)//T):
    count = 0
    while j < n and count < T:
        print(p[j], end='')
        j += 1
        count += 1
    if i < (n+T-1)//T-1:
        print(' ', end='')
print()
