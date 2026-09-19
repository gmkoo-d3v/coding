def solution(num_list):
    evens = []
    odds = []

    for i in num_list:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)

    answer = []
    answer.append(len(evens))
    answer.append(len(odds))

    return answer