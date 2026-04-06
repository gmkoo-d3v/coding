N, B = map(int, input().split())
if N == 0:
    print(0)
else:
    result = ""
    while N > 0:
        divider = N % B

        if divider < 10:
            result = str(divider) + result
        else:
            result = chr(divider - 10 + ord('A'))+result
        N //= B
    print(result)