import sys

arinput = sys.stdin.read().split()

N = int(arinput[0])
number = list(map(int, arinput[1:N+1]))
v = int(arinput[N+1])

print(number.count(v))
