import sys

str = sys.stdin.readlines()

s = str[0]
t = str[1]
count = 0
for i in range(3):
    if s[i]==t[i]:
        count += 1

print(count)
