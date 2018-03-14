import sys
from random import randint


# n -> length of array
# mult -> desired number
# lim -> limit of numbers in array
n, mult, lim = map(int, sys.argv[1:4])
ar = []
print(n, mult)
for _ in range(n):
    ar.append(randint(0, lim))
print(" ".join(map(str, ar)))
