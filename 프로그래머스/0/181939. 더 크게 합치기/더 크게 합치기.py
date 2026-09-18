def solution(a, b):
    answer = 0
    aa = str(a)+str(b)
    bb = str(b)+str(a)
    if int(aa)>int(bb):
        return int(aa)
    else:
        return int(bb)