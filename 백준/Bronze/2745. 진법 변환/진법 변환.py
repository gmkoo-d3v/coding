N, B = input().split()
B = int(B)
result = 0

for char in N:
    if char.isdigit():
        value = int(char)
    else:
        value = ord(char) - ord('A') + 10
    result = result * B + value
print(result)    