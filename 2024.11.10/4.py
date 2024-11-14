def countable_nouns(num: int, noun: tuple[str, str, str]) -> str:
    """
    Функция,возвращающая существительное русского языка, 
    согласованное с числом.
    
        exceptions - исключения
        noun_two - окончание чисел для слова 'года'
        noun_two - окончание чисел для слова 'лет'
    """
    
    exceptions = ['11', '12', '13', '14']
    noun_two = ['2', '3', '4']
    noun_three = ['0', '5', '6', '7', '8', '9']
    
    num = str(num)
    
    if num[-1] == '1' and num not in exceptions:
        return noun[0]
    elif num[-1] in noun_two and num != exceptions:
        return noun[1]
    elif num[-1] in noun_three or num in exceptions:
        return noun[2]
        
countable_nouns()

#>>> countable_nouns(1, ("год", "года", "лет"))
#'год'
#>>> countable_nouns(11, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(659, ("год", "года", "лет"))
#'лет'
#>>> countable_nouns(22, ("год", "года", "лет"))
#'года'


