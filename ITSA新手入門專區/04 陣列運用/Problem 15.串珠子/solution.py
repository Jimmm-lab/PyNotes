l = list(map(int, input().split()))

B = {}
for num in l:
    if num in B:
        B[num] += 1
    else:
        B[num] = 1

for k, v in B.items():
    if v < 3:
        print(k)
        break
