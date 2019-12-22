import sys

str = sys.stdin.readlines()

n = int(str[0])
alist_str = str[1].split()

target = 1
breaks = 0
for a in alist_str:
    if int(a) == target:
        target += 1
    else:
        breaks += 1

if breaks == n:
    print(-1)
else:
    print(breaks)