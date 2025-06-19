A, B, C = map(int, input().split())

SUM = A+B+C
if SUM <= 9:
    print(SUM, "L")
else:
    print(SUM, "H")
