n, mult = map(int, input().split())
ar = list(map(int, input().split()))
res = 0

for i in range(n-1):
    for j in range(i+1, n):
        if ar[i]*ar[j] == mult:
            res += 1

print(res)
