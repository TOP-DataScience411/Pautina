n = int(input())
num1 = num2 = 1
for _ in range(n):
    print(num1, end = ' ')
    num1, num2 = num2, num1 + num2

#17
#1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597