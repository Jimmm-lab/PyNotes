n = int(input())

MAX = total = PASS = 0
MIN = 100
i = 0
while i < n:
    S = int(input())
    if S > MAX:
        MAX = S
    if S < MIN:
        MIN = S
    if S >= 60:
        PASS += 1
    total += S
    i += 1
avg = round(total/n, 1)

print(f"Max:{MAX}\nMin:{MIN}\nAverage:{avg}\nPass:{PASS}")
