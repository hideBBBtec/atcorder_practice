import sys
import fractions

str = sys.stdin.readline()

a = int(str.split()[0])
b = int(str.split()[1])

print((a * b) // fractions.gcd(a,b))

