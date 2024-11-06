num1, num2 = int(input()), int(input())
if num1 % num2 == 0:
    print(f'{num1} делится на {num2} нецело\nчастное: {num1//num2}')
elif num2 % num1 == 0:
    print(f'{num2} делится на {num1} нецело\nчастное: {num2//num1}')
elif num1 > num2 and num1 % num2 != 0:
    print(f'{num1} не делится на {num2} нацело\nнеполное частное: {num1 // num2}\nостаток: {num1 % num2}')
elif num2 > num1 and num2 % num1 != 0:
    print(f'{num2} не делится на {num1} нацело\nнеполное частное: {num2 // num1}\nостаток: {num2 % num1}')

#8
#2
#8 делится на 2 нецело
#частное: 4

#10
#3
#10 не делится на 3 нацело
#неполное частное: 3
#остаток: 1
