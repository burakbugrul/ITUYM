from collections import defaultdict

n, mult = map(int, input().split())
count = defaultdict(int)
ar = list(map(int, input().split()))
res, ind = 0, 0

for item in ar:

    if mult == 0 and item != 0:
        res += count[0]
    elif mult == 0 and item == 0:
        res += ind
    elif item != 0 and mult%item == 0:
        res += count[mult//item]

    ind += 1
    count[item] += 1

print(res)
