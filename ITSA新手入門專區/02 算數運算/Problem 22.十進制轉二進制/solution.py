d = int(input())

def binary(d):
    s = ''
    while d > 0:
        s += str(d % 2)
        d //= 2
        
    return s

def binaryAddOne(c):
    d = list(c)
    flag = True
    for i in range(0, len(d)):
        if d[i] == '0' and flag:
            d[i] = '1'
            d = d[::-1]
            flag = False
            break
        elif d[i] == '1' and flag:
            d[i] = '0'
            
    if flag:
        d = d[::-1]
        d.append('1')
        
    return ''.join(d)

if d < 0:
    b = binary(-d)
    while len(b) != 8:
        b += '0'

    c = ''
    for ch in b:
        if ch == '1':
            c += '0'
        else:
            c += '1'
    print(binaryAddOne(c))
    
else:
    b = binary(d)
    while len(b) != 8:
        b += '0'
    print(b[::-1])
