hs, ms = map(int, input().split())
he, me = map(int, input().split())

d = (he-hs)*60+me-ms
c = d
cost = 0
if d <= 120:
    cost += d//30*30
elif d <= 240:
    cost += 120
    c -= 120
    cost += c//30*40
elif d > 240:
    cost += 280
    c -= 240
    cost += c//30*60

print(cost)
