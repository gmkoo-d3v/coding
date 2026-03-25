arrword = [input() for _ in range(5)]

m_len = max(len(word) for word in arrword)

for col in range(m_len):
    for row in range(5):
        if col < len(arrword[row]):
            print(arrword[row][col], end='')
