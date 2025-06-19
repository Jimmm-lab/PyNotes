N = input()

def isArmstrong(N):
    sum = 0
    for ch in N:
        sum += int(ch)**3
    if sum == int(N):
        return True
    return False

if isArmstrong(N):
    print('YES')
else:
    print('NO')
