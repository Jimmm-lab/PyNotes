N = int(input())

l = []
while N > 0:
    l.append(int(input()))
    N -= 1

l.sort(reverse=True)
for num in l:
    print(num, end='')
print()
