def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1
        if start > 0:
            count += 1
        else:
            return count


n, m = map(int, input().split())
text, pattern = input(), input()
res = 0
for i in range(len(pattern)):
    for j in range(i, len(pattern)):
        res += occurrences(text, pattern[i:j+1])
print(res)
