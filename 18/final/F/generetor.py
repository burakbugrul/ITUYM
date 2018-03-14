import sys
from random import choice
from string import ascii_lowercase


# n -> length of first string
# m -> length of second string
# lim -> maximum number of characters from alphabet used
n, m, lim = map(int, sys.argv[1:4])
print(n, m)
print(''.join(choice(ascii_lowercase[:min(lim, len(ascii_lowercase))]) for _ in range(n)))
print(''.join(choice(ascii_lowercase[:min(lim, len(ascii_lowercase))]) for _ in range(m)))
