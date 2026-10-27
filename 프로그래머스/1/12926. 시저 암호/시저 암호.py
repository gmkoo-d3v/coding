def solution(s, n):
    answer = ""

    for ch in s:
        if 'A' <= ch <= 'Z':
            if ord(ch) + n > ord('Z'):
                answer += chr(ord(ch) + n - ord('Z') - 1 + ord('A'))
            else:
                answer += chr(ord(ch) + n)

        elif 'a' <= ch <= 'z':
            if ord(ch) + n > ord('z'):
                answer += chr(ord(ch) + n - ord('z') - 1 + ord('a'))
            else:
                answer += chr(ord(ch) + n)

        else:
            answer += ch

    return answer