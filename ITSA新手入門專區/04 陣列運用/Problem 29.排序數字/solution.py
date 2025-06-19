N = int(input())
Nums = list(map(int, input().split()))
M = int(input())

Nums.append(M)
Nums.sort()
for num in Nums:
    print(num, end='')
    if N > 0:
        print(',', end='')
    N -= 1
print()
