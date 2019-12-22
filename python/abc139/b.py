import sys

# -----------------------------------------
import os
fdr = os.open('python/abc139/sample.txt', os.O_RDONLY)
os.dup2(fdr, sys.stdin.fileno())
# -----------------------------------------

str = sys.stdin.readline().split()

A = int(str[0])
B = int(str[1])
c = (B-1) // (A-1)
if (B-1)%(A-1) != 0:
    c+=1

print(c)
