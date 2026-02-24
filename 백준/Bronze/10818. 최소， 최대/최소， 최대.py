import sys

data = sys.stdin.buffer.read().split()
N = int(data[0])
arr = list(map(int,data[1:1+N]))
mn=min(arr)
mx=max(arr)
sys.stdout.write(f"{mn} {mx}")