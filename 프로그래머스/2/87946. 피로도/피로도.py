from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons):
        exhaustion = k
        count = 0

        for required, cost in order:
            if exhaustion >= required:
                exhaustion -= cost
                count += 1
            else:
                break

        answer = max(answer, count)

    return answer
