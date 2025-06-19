N = int(input())
girls = list(input().split())
K = input()

count = 0
for girl in girls:
    flag = True
    for c in K:
        if c not in girl:
            flag = False
            break
    if flag:
        count += 1

print(count)
