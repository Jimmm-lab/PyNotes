n = int(input())
F = list(map(int, input().split()))
start, stop = map(int, input().split())

sum = 0
for i in range(start-1, stop):
    sum += F[i]
print(sum)
