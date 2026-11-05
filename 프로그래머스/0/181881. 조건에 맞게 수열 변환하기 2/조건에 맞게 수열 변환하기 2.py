def solution(arr):
    count = 0

    while True:
        answer = []

        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                answer.append(arr[i] // 2)
            elif arr[i] < 50 and arr[i] % 2 != 0:
                answer.append(arr[i] * 2 + 1)
            else:
                answer.append(arr[i])

        if arr == answer:
            return count

        arr = answer
        count += 1