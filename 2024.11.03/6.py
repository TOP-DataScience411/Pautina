num = input()

nums = [int(num[:3][i]) for i in range(3)]
nums2 = [int(num[3:][i]) for i in range(3)]
print('да' if sum(nums) == sum(nums2) else 'нет')

#183534
#да

#401367
#нет