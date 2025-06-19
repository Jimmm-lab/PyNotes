a, b, c = map(int, input().split())
X, Y = map(int, input().split())

def isOnLine(a, b, c, X, Y):
    if a*X+b*Y == -c:
        return True
    return False

if isOnLine(a, b, c, X, Y):
    print('YES')
else:
    print('NO')
