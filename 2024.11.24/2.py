def product(nums) -> float:
    """
    Рекурсивная функция, возвращающая произведение чисел.
    Функция принимает обязательным позиционно-ключевым аргументом итерируемый объект с числами в качестве элементов.

    """
    if len(nums) == 1:
        return nums[0]
    return float(nums[0] * abs(product(nums[1:])))

#>>> product(range(10, 60, 10))
#12000000.0
#>>> product((0.12, 0.05, -0.09, 0.0, 0.21))
#0.0