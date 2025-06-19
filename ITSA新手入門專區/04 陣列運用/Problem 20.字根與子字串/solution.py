s = input()
t = input()

'''def isSubstring(s, t):
    for i in range(len(t)-len(s)+1):
        flag = False
        for j in range(0, len(s)):
            if s[j] == t[i+j]:
                flag = True
            else:
                flag = False
        if flag:
            return "YES"
    return "NO"'''

def isSubstring(s, t):
    return "YES" if s in t else "NO"

print(isSubstring(s, t))
