nums = []
while True:
    num = int(input())
    if num % 7 == 0:
        nums.append(num)
    else:
        break
print(*nums[::-1])

#7
#7
#14
#21
#13
#21 14 7 7