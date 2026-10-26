def solution(absolutes, signs):
    temp = 0
    for i in range(len(absolutes)):
        if signs[i]:
            temp += absolutes[i]
        else:
            temp -= absolutes[i]
    return temp
        