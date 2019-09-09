import sys

# -----------------------------------------
import os
fdr = os.open('python/abc139/sample.txt', os.O_RDONLY)
os.dup2(fdr, sys.stdin.fileno())
# -----------------------------------------

str = sys.stdin.readlines()

N = int(str[0])
Hs = str[1].split()

Hnum = []
Hnum.append(int(Hs[0]))
j = 0
tmpcount = 0
maxcount = 0
for i in range(1,N+1):
    if i == N:
        Hnum.append(Hnum[N-1] + 1)
    else:
        Hnum.append(int(Hs[i]))
    if Hnum[i]>Hnum[i-1]:
        tmpcount = i - j - 1
        if tmpcount > maxcount:
            maxcount = tmpcount
        j = i

print(maxcount)
