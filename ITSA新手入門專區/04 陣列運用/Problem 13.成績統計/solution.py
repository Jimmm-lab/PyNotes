x = int(input())

i = avgTotal = 0
avgC = avgE = avgM = 0
while i < x:
    C, E, M = map(int, input().split())
    avgC += C
    avgE += E
    avgM += M
    avgTotal += (C+E+M)/3
    i += 1
avgC = round(avgC/x, 1)
avgE = round(avgE/x, 1)
avgM = round(avgM/x, 1)
avgTotal = round(avgTotal/x, 1)

print(f"{avgTotal} {avgC} {avgE} {avgM}")
