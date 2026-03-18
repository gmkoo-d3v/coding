nums = list(map(int,input().split()))
chess = [1,1,2,2,2,8]
count = []
for i in range(len(nums)):
    count.append(chess[i]-nums[i])
print(*count)