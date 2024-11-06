year = int(input())
print('да' if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 'нет')

#2020
#да