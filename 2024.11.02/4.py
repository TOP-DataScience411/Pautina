hor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
ver = ['1', '2', '3', '4', '5', '6', '7', '8']

one, two = input(), input()

print(
'да' if 
(hor.index(one[0]) + 
ver.index(one[1]) + 
hor.index(two[0])+ 
ver.index(two[1]) + 4) % 2 == 0 
else 'нет'
)

#a1
#b2
#да