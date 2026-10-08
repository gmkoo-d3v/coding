def solution(number):
    temp = 0
    for i in range(len(number)):
        temp += int(number[i])
    return temp % 9        