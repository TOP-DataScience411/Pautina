from decimal import Decimal
from datetime import date, time, datetime
import numbers

class PowerMeter:
    def __init__(self,
                 tariff1: numbers.Number = 6.5,
                 tariff2: numbers.Number = 4.10,
                 tariff2_starts: time = time(7, 0),
                 tariff2_ends: time = time(23, 0),
                 ):

        self.tariff1 = Decimal(tariff1)
        self.tariff2 = Decimal(tariff2)
        self.tariff2_starts = tariff2_starts
        self.tariff2_ends = tariff2_ends
        self.power = Decimal(0)
        self.charges: dict[date, Decimal] = {}

    def meter(self, power: Decimal) -> Decimal:

        """Функция принимает значение потреблённой мощности, 
        вычисляет и возвращает стоимость согласно тарифному плану, 
        действующему в текущий момент"""

        self.power += Decimal(power)
        if self.tariff2_starts >= datetime.now().time() <= self.tariff2_ends:
            charge = Decimal(power) * self.tariff2
        else:
            charge = Decimal(power) * self.tariff1

        today = date.today()

        if today in self.charges:
            self.charges[today] += charge
        else:
            self.charges[today] = charge
        return charge.quantize(Decimal('0.01'))

    def __repr__(self) -> str:

        """Возвращает машиночитаемое строковое представление"""

        return f"<PowerMeter: {self.power.quantize(Decimal('0.01'))} кВт/ч>"

    def __str__(self) -> str:

        """Возвращает человекочитаемое строковое представление"""

        month = datetime.now().strftime('%b')
        costs = sum(charge for day, charge in self.charges.items() if day.month == datetime.now().month)
        return f"({month}) {costs.quantize(Decimal('0.01'))}"


#>>> pm1 = PowerMeter()
#>>> pm1.meter(2)
#Decimal('13.00')
#>>> pm1.meter(1.2)
#Decimal('7.80')
#>>> pm1
#<PowerMeter: 3.20 кВт/ч>
#>>> print(pm1)
#(Jan) 20.80