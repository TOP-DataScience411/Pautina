num = int(input())
# ИСПРАВИТЬ: повторное вычисление одних и тех же объектов неоптимально
print(f"Сумма цифр = {num // 100 + num // 10 % 10 + num % 10} \nПроизведение цифр = {(num // 100) * (num // 10 % 10) * (num % 10)}")


#Сумма цифр = 9
#Произведение цифр = 27


# ИТОГ: доработать — 3/4

