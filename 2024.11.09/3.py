nums1, nums2 = [list(map(int, input().split())) for _ in range(2)]
nums1_step = set([elem + 1 for elem in nums1])
print(('да', 'нет')[nums1_step.issuperset(nums2)])

#1 2 3 4
#1 2
#да

#1 2 3 4
#2 4
#нет