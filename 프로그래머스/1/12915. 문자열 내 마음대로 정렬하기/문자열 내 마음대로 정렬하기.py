def solution(s, n):
    return sorted(s, key=lambda s: (ord(s[n]), s))