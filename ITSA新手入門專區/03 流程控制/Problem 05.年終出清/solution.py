P = int(input())

if P < 10:
    print(P*100)
elif P >= 10 and P <= 29:
    print(int(P*100*0.9))
elif P >= 30 and P <= 99:
    print(int(P*100*0.8))
else:
    print(int(P*100*0.7))
