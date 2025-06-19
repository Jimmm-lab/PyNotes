x = input()

def isInt(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

if isInt(x):
    print('int')
elif isFloat(x):
    print('float')
elif len(x) == 1:
    print('char')
else:
    print('string')
