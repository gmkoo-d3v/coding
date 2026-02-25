import sys

numb=[]
for _ in range(9):
    i = int(input())
    numb.append(i)
print(max(numb))
print(numb.index(max(numb))+1)