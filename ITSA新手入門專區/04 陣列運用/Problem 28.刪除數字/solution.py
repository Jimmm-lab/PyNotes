a, b = input().split(',')
b = int(b)

stack = []
remove = int(b)

for digit in a:
    while stack and remove > 0 and stack[-1] > digit:
        stack.pop()
        remove -= 1
    stack.append(digit)

# 補上沒刪夠的（從尾巴刪）
while remove > 0:
    stack.pop()
    remove -= 1

# 組合起來 & 去掉前導 0
result = ''.join(stack).lstrip('0')
print(result if result else '0')
