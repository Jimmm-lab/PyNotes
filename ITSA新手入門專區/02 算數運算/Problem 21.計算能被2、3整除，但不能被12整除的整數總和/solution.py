N = int(input())

sum = 0
for i in range(1, N+1):
    if i % 6 == 0 and i % 12 != 0:
        sum += i

print(sum)   
