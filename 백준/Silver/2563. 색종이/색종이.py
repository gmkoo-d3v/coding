n = int(input())
paper = []

for i in range(100):
    row=[]
    for j in range(100):
        row.append(0)
    paper.append(row)

for j in range(n):
    x, y = map(int, input().split())

    for k in range(x, x+10):
        for l in range(y, y+10):
            paper[k][l] = 1

result=0
for m in range(100):
    result += sum(paper[m])

print(result)