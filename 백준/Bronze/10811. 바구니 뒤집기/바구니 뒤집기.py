N,M = map(int, input().split())

numbs = [i for i in range(1, N+1)]


for i in range(M):
    j, k = map(int, input().split())
    temp = numbs[j-1:k]
    temp.reverse()
    numbs[j-1:k] = temp
 
for i in range(N):
    print(numbs[i], end = " ")