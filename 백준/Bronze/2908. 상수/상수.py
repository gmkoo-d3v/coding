A,B = input().split()

AA = int(A[::-1])
BB = int(B[::-1])

print(AA if AA >= BB else BB)