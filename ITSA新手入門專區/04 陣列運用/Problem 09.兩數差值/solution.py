N = list(input().split(','))

N.sort(reverse=True)
MAX = int(''.join(N))

N.sort()
MIN = int(''.join(N))
print(MAX-MIN)
