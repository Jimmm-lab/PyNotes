m = int(input())

p = []
for _ in range(m):
    a, b = map(int, input().split())
    p.append((a, b))

def total_covered_length(segments):
    # 先按起點排序
    segments.sort()
    
    merged = []
    for start, end in segments:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    
    # 計算總長
    total = 0
    for s, e in merged:
        total += e - s
    return total

print(total_covered_length(p))  # Output: 9
