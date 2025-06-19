k = int(input())
n = list(map(int, input().split()))

def minDiff(n):
    total = sum(n)
    target = total // 2 #目標是找到一組數字，它的加總最接近 total/2
    dp = [False] * (target+1)
    dp[0] = True # 0 元一定可以組出來（因為什麼都不拿）

    for num in n:
        for i in range(target, num-1, -1):
            dp[i] = dp[i] or dp[i-num]

    for j in range(target, -1, -1):
        if dp[j]:
            return total-2*j

print(minDiff(n))

'''totalVal = sum(n)
MIN = float('inf')
for i in range(0, k-2):
    for j in range(i+1, k-1):
        for k in range(j+1, k):
            diff = abs(n[i]+n[j]+n[k]-(totalVal-n[i]-n[j]-n[k]))
            if diff < MIN:
                MIN = diff

print(MIN)'''
