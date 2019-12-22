import sys

str = sys.stdin.readline()

N = int(str)

if N % 2 != 0:
    print(0)
else:
    k = 10
    ans = 0
    while k <= N:
        ans += (N - (N % k)) // k
        k = k * 5

    print(ans)