binary = {'1', '0'}

def check(s):
    a = set(s)
    if set(s) <= binary or s[0] == 'b' or s[:2] == '0b':
        return 'да'
    else:
        return 'нет'
        
print(check(input().strip()))

#0101
#да

#1b0
#нет