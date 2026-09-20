def solution(array):
    count = {}

    for num in array:
        count[num] = count.get(num, 0) + 1

    max_count = max(count.values())

    modes = []

    for num, cnt in count.items():
        if cnt == max_count:
            modes.append(num)

    if len(modes) == 1:
        return modes[0]

    return -1