def solution(str1, str2):
    answer = ''
    for number in range(len(str1)):
        answer += str1[number] +str2[number] 
    return answer
