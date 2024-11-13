from collections import Counter
names = input().strip().split('; ')
dct = Counter(names)
list = []
for k, v in dct.items():
    while (v) > 1:
        index = k.find('.')
        list.append(f'{k[:index]}_{v}{k[index:]}')
        v -= 1
    if v == 1:
       list.append(k)
print(*sorted(list), sep= '\n')

#   1.py; 1.py; src.tar.gz; aux.h; main.cpp; functions.h; main.cpp; 1.py; main.cpp; src.tar
#1.py
#1_2.py
#1_3.py
#aux.h
#functions.h
#main.cpp
#main_2.cpp
#main_3.cpp
#src.tar
#src.tar.gz