def solution(s, p):
    ss = s.lower()
    pp = p.lower()
    if ss.find(pp) != -1:
        return 1
    else:
        return 0