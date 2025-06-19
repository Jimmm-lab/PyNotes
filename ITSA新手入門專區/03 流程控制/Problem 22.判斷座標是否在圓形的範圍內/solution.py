X, Y = map(int, input().split())

def isInsideCircle(X, Y):
    if X**2+Y**2 <= 100**2:
        print('inside')
    else:
        print('outside')

isInsideCircle(X, Y)
