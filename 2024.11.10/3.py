def numbers_strip(nums: list[float], n: int = 1, *, copy: bool = False) -> list:
    """
    Функция, принимающая список вещественных чисел и, 
    удаляет n минимальных и n максимальных чисел из списка.
    Возвращает исходный объект списка с внесёнными изменениями
    или изменённую копию (новый объект) исходного списка.
    """
    if copy == False:
        while n != 0:
            nums.remove(max(nums))
            nums.remove(min(nums))
            n -= 1
        return nums
        id(nums)
    elif copy == True:
        nums_copy = nums.copy()
        while n != 0:
            nums_copy.remove(max(nums_copy))
            nums_copy.remove(min(nums_copy))
            n -= 1
        return nums_copy
    
numbers_strip()


#>>> list =[1.0, 2.0, 3.0, 4.0, 5.0]
#>>> test = numbers_strip(list)
#>>> test
#[2.0, 3.0, 4.0]
#>>> list is test
#True

#>>> list = [18.0, 11.0, 25.0, 4.0, 96.0]
#>>> test = numbers_strip(list, 2, copy=True)
#>>> test
#[18.0]
#>>> list is test
#False