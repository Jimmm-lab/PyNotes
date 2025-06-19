n = int(input())
coins = list(map(int, input().split()))
p = int(input())

def getCoinState(coins, n, rest, s, t):
    if n == 0:
        if rest >= 0:
            s.append(rest)
            t.append(s)
        return
    
    coin = coins[n]
    for i in range(0, rest//coin+1):
        getCoinState(coins, n-1, rest-i*coin, s+[i], t)
    
t = []
getCoinState(sorted(coins), n-1, p, [], t)

if coins[0] < coins[1]:
    for i in range(0, len(t)):
        t[i] = t[i][::-1]
    
t = sorted(t, key=lambda x: x)

for l in t:
    print('(', l[0], sep='', end='')
    for i in range(1, len(l)):
        print(',', l[i], sep='', end='')
    print(')')

'''for i in range(0, p//coins[n-1]+1):
    for j in range(0, p//coins[n-2]+1):
        v = p
        if p-j*coins[n-2]-i*coins[n-1] < 0:
            continue
        else:
            v -= j*coins[n-2]+i*coins[n-1]
            print('(', v, ',', j, ',', i, ')', sep='')'''
