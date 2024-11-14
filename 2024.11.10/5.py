import math

def central_tendency(num1, num2: float, *nums: float) -> dict[str, int]:
    """ 
    Функция, вычисляющая основные меры центральной тенденции для некоторого количества чисел.
    Возвращает словарь с подписанными вычисленными значениями мер центральной тенденции.
    
        'median' — медиана
        'arithmetic' — среднее арифметическое
        'geometric' — среднее геометрическое
        'harmonic' — среднее гармоническое
    """
    keys = ['median', 'arithmetic', 'geometric', 'harmonic']

    nums = sorted((num1, num2) + nums)
    
    if len(nums) % 2 != 0:
        med = float(nums[int(len(nums) / 2)])
    else:
        med = (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2) - 1]) / 2
    
    arith = sum(nums) / len(nums)
    geom = (math.prod(nums)) ** (1/len(nums))
    harm = len(nums) / (sum([1/elem for elem in nums]))
    
    values = [med, arith, geom, harm]
    
    print(dict(zip(keys, values)), sep= ',')
    
    
(central_tendency())

#{'median': 2.5, 'arithmetic': 2.5, 'geometric': 2.213363839400643, 'harmonic': 1.92}
#>>> test = [1, 2, 3, 4, 5]
#>>> central_tendency(*test)
#{'median': 3.0, 'arithmetic': 3.0, 'geometric': 2.605171084697352, 'harmonic': 2.18978102189781}
