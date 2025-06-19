A, B, C = map(int, input().split())

def isRightTriangle(A, B, C):
    if A**2+B**2 == C**2:
        return True
    return False

def isObtuseTriangle(A, B, C):
    if A**2+B**2 < C**2:
        return True
    return False

def isAcuteTriangle(A, B, C):
    if A**2+B**2 < C**2:
        return False
    if A**2+C**2 < B**2:
        return False
    if B**2+C**2 < A**2:
        return False
    return True

if isRightTriangle(A, B, C):
    print('Right Triangle')
elif isObtuseTriangle(A, B, C):
    print('Obtuse Triangle')
elif isAcuteTriangle(A, B, C):
    print('Acute Triangle')
else:
    print('Not Triangle')
