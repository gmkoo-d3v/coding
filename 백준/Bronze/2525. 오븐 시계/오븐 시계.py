A,B=map(int,input().split())
C=int(input())

D=(A*60+B+C)%(24*60)

print(D//60,D%60)