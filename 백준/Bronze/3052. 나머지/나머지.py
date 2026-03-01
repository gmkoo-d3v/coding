arr = set()

for i in range(10):
    A = int(input())
    arr.add(A % 42)
print(len(arr))
