def solution(array):

    dic = {}
    for num in array:
        dic[num] = array.count(num)
    
    max_count = max(dic.values())
    
    answer = []
    for i, cnt in dic.items():
        if cnt == max_count:
            answer.append(i)
    if len(answer) == 1:
        return answer[0]
    return -1
    