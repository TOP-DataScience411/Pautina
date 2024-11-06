s = input()
cost = 30 * len([i for i in range(len(s)) if s[i].isalnum()])
print(f'{cost // 100} руб. {cost - 100 * (cost // 100)} коп.')

#    грузите апельсины бочках братья карамазовы
#11 руб. 40 коп.