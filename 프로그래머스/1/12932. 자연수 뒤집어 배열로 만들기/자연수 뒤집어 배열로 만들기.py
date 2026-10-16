def solution(n):
    temp = str(n)
    answer = []
    
    for i in temp[::-1]:
        answer.append(int(i))
    return answer