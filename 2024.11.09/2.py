fruits = []
while True:
    fruit = input()
    if fruit != '':
        fruits.append(fruit)
    else:
        break
    
if len(fruits) == 1:
    print(*fruits)
elif len(fruits) == 2:
    print(f'{fruits[0]} и {fruits[1]}')
else:
    print(*fruits[:-1], sep= ', ', end= ' и ')
    print(*fruits[-1:])

#apple
#
#apple

#apple
#banana
#
#apple и banana

#apple
#banana
#peach
#
#apple, banana и peach