def solution(a, d, included):
    adder = 0
    for i, checker in enumerate(included):
        if checker == True:
            adder += a+d*i
    return adder