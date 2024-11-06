n = int(input())
nums = [int(input()) for _ in range(n)]
print(sum([nums[i] for i in range(len(nums)) if nums[i] > 0]))

#6
#3
#-5
#1
#10
#-1
#8
#22