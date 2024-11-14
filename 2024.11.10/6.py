def orth_triangle(*, cathetus1: float = None, cathetus2: float = None, hypotenuse: float = None) -> float:
    """ 
    Функция, вычисляющая третью сторону прямоугольного треугольника по двум переданным.
    Функция возвращает длину третьей стороны треугольника или None, если вычисление невозможно.
    """
    if cathetus1 and cathetus2 != None:
        return ((cathetus1 ** 2) + (cathetus2 ** 2)) ** 0.5
        
    elif cathetus1 and hypotenuse != None and cathetus1 < hypotenuse:
        return ((hypotenuse ** 2) - (cathetus1 ** 2)) ** 0.5
        

    elif cathetus2 and hypotenuse != None and cathetus2 < hypotenuse:
        return ((hypotenuse ** 2) - (cathetus2 ** 2)) ** 0.5


orth_triangle()

#>>> orth_triangle(cathetus1=3, hypotenuse=5)
#4.0
#>>> orth_triangle(cathetus1=8, cathetus2=15)
#17.0
#>>> print(orth_triangle(cathetus2=9, hypotenuse=3))
#None


