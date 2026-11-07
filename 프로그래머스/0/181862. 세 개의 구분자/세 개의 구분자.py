def solution(myStr):
    answer = []
    current = []
    
    for i in myStr:
        if i in "abc":
            if current:
                answer.append("".join(current))
                current = []
        else: current.append(i)
    
    if current:
        answer.append("".join(current))
    
    return answer if answer else ["EMPTY"]