A, B, C = map(int, input().split())

def isTriangle(A, B, C):
    if A+B <= C:
        return False
    if A+C <= B:
        return False
    if B+C <= A:
        return False
    return True

if isTriangle(A, B, C):
    print('fit')
else:
    print('unfit')
