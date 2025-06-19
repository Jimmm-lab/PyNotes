s = input()
rs = s[::-1]
i = 0
for ch in rs:
    print(ch, sep='', end='')
    if i < len(s)-1:
        print(',', sep='', end='')
        i += 1
print()
