def solution(score):
    avg = []
    for i,j in score:
        avg.append(i+j)
    
    sort_avg = sorted(avg, reverse = True)
    
    answer = []
    for k in avg:
        rank = sort_avg.index(k)+1
        answer.append(rank)
    return answer