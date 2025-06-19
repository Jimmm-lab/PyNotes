n = int(input())
M = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s = (set(M) & set(A)) | (set(M) & set(B))
print(len(s))
