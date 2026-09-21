def solution(numLog):
    result = ""
    for i in range(len(numLog)-1):
        stage = numLog[i+1] - numLog[i]
        if stage == 1:
            result += 'w'
        elif stage == -1:
            result += 's'
        elif stage == 10:
            result += 'd'
        elif stage == -10:
            result += 'a'
    return result