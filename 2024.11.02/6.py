hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ver = ['1', '2', '3', '4', '5', '6', '7', '8']
one, two = input(), input()

print(
'да' if 
-1 <= (hor.index(one[0]) + 1) - (hor.index(two[0]) + 1) <= 1 
and 
-1 <= (ver.index(one[1]) + 1) - (ver.index(two[1]) + 1) <= 1 
else 'нет')

#g3
#f2
#да

#c6
#d4
#нет