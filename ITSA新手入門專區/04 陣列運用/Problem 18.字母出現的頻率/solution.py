s = input().upper()

alphabet = {chr(i): 0 for i in range(ord('A'), ord('Z')+1)}
for ch in s:
    if ch in alphabet:
        alphabet[ch] += 1

print(''.join(f" {v}" for v in alphabet.values()).lstrip())
