import sys

str = sys.stdin.readlines()

n = int(str[0])
strs = str[1].split()
s = strs[0]
t = strs[1]

string = ""
for i in range(n):
    string += s[i] + t[i]

print(string)
