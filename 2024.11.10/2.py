def taxi_cost(m: int, t: int = 0) -> int | None:
    base_cost = 80
    add_cost = 6
    vait_cost = 3
    cancel = 80
    """ 
    Вычисляет стоимость поездки на такси и возвращает стоимость, 
    округляется до целого числа.
    
        Обязательный аргумент:
        m (int): длина маршрута в метрах
        Необязательнй аргумент (по умолчанию = 0):
        t (int): длительность ожидания в минутах
            
            Значения для рассета стоимости:
            base_cost = базовая стоимость поездки 80 рублей
            add_cost = за каждые 150 метров к стоимости добавляется 6 рублей
            vait_cost = за каждую минуту ожидания к стоимости добавляется 3 рубля
            cancel = при отмене поездки (длина маршрута составила 0 метров) к стоимости добавляется штраф 80 рублей и стоимость времени ожидания
    """
    if m < 0:
        return 
    elif m == 0:
        return int(base_cost + cancel + t * vait_cost)
    else:
        return (int(base_cost + t * vait_cost) if m == 300 else int(base_cost + ((m / 150) * add_cost) + t * vait_cost)) 
    
print(taxi_cost(int(input()))) 
    
#-300
#None
#>>> taxi_cost(42130, 8)
#1789
#>>> taxi_cost(1500)
#140
#>>> taxi_cost(0, 5)
#175



