L, P = map(int, input().split())
news = list(map(int, input().split()))

actual = L * P

for i in news:
    print(i - actual, end =" ")