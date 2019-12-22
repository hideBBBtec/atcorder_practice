import sys

str = sys.stdin.readlines()

list = [int(str[0]), int(str[1]) ]

if 1 not in list:
    print(1)
elif 2 not in list:
    print(2)
else:
    print(3)
