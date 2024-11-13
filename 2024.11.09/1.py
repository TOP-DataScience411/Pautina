email = input()
symbol1_index = email.find('@')
symbol2_index = email[symbol1_index:].find('.')
print('ндеат'[symbol1_index != -1 and symbol2_index != -1::2])

#gd@ya.
#да
#abcde@fg
#нет