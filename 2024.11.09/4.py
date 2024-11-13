dct = {}
while True:
    s = input().split()
    if s != []:
        dct[s[0]] = s[1:]
    else:
        break
try:
    print(list(dct.keys())[list(dct.values()).index(list(input().split()))])
except ValueError:
    print('! value error !')

#  1004 ER_CANT_CREATE_F
#  1006 ER_CANT_CREATE
#  1005 ER_CANT_CREATE_TA
#  1007 ER_DB_CREATE_EXI
#
#  ER_CANT_CREATE
#1006

#  1004 ER_CANT_CREATE_F
#  1007 ER_DB_CREATE_EX


#  ER_CANT_CREATE
#! value error !