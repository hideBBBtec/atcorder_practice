import sys

# -----------------------------------------
import os
fdr = os.open('python/abc139/sample.txt', os.O_RDONLY)
os.dup2(fdr, sys.stdin.fileno())
# -----------------------------------------

str = sys.stdin.readlines()
