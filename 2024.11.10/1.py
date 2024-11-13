def strong_password(password: str) -> bool: 
    """
    Принимает пароль в формате строки и прверяет на надежность:
    - длина от 8 символов
    - наличие буквенных символов в обоих регистрах
    - наличие от двух символов цифр
    - наличие символов прочих категорий (пробел, знаки пунктуации,и т.п.)
        """
    cnt_d = 0
    cnt_s = 0
    if len(password) < 8:
        return False
    for elem in password:
        if elem.isdigit():
            cnt_d += 1
        elif elem.isalnum() == False:
            cnt_s += 1
    return cnt_d > 1 and cnt_s > 0 and password.islower() == False and password.isupper() == False #bool
    
print(strong_password(input()))

#aP3:kD_l3
#True

#password
#False