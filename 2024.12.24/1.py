class Point:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x
    @x.setter
    def x(self, value) -> None:
        raise TypeError("'Point' object does not support coordinate assignment")

    @property
    def y(self) -> float:
        return self._y
    @y.setter
    def y(self, value) -> None:
        raise TypeError("'Point' object does not support coordinate assignment")

    def __repr__(self) -> str:
        return f'({self._x},{self._y})'
    def __str__(self) -> str:
        return f'({self._x},{self._y})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Point):
            return self._x == other.x and self._y == other.y
        return False

class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length: float =  self._length_calc(start, end)

    @property
    def start(self) -> Point:
        return self._start
    @start.setter
    def start(self, new_point: Point) -> None:
        if isinstance(new_point, Point):
            self._start = new_point
            self._length = self._length_calc(self._start, self._end)
        else:
            raise TypeError("'start' attribute of 'Line' object supports only 'Point' object assignment")

    @property
    def end(self) -> Point:
        return self._end
    @end.setter
    def end(self, new_point) -> None:
        if isinstance(new_point, Point):
            self._start = new_point
        else:
            raise TypeError("'end' attribute of 'Line' object supports only 'Point' object assignment")

    @property
    def length(self) -> float:
        return self._length
    @length.setter
    def length(self, value) -> None:
        raise TypeError("'Line' object does not support length assignment")

    def __repr__(self) -> str:
        return f'{self._start}———{self._end}'
    def __str__(self) -> str:
        return f'{self._start}———{self._end}'

    @staticmethod
    def _length_calc(start: Point, end: Point) -> float:
        return ((start.x - end.x) ** 2 + (start.y - end.y) ** 2) ** 0.5

class Polygon(list):
    def __init__(self, side1: Line, side2: Line, side3: Line, *sides: Line):
        sides = [side1, side2, side3] + list(sides)
        if len(sides) < 3:
            raise ValueError("A polygon must have at least three sides.")
        self._sides = sides
        super().__init__(self._sides)
        self.is_closed()

    @property
    def perimeter(self) -> float:

        """Вычисляет периметр многоугольника"""

        self.is_closed()
        return sum(line.length for line in self)

    def is_closed(self):

        """Проверяет, формируют ли отрезки замкнутый многоугольник"""

        for i in range(len(self) - 1):
            if self[i].end != self[i + 1].start:
                raise ValueError("items doesn't form a closed polygon")


#>>> p1 = Point(0, 3)
#>>> p2 = Point(4, 0)
#>>> p3 = Point(8, 3)
#>>> p1
#(0,3)
#>>> repr(p1) == str(p1)
#True
#>>> p1 == Point(0, 3)
#True
#>>> p1.x, p1.y
#(0, 3)
#>>> p2.y = 5
#TypeError: 'Point' object does not support coordinate assignment
#>>> l1 = Line(p1, p2)
#>>> l2 = Line(p2, p3)
#>>> l3 = Line(p3, p1)
#>>> l1
#(0,3)———(4,0)
#>>> repr(l1) == str(l1)
#True
#>>> l1.length
#5.0
#>>> l1.length = 10
#TypeError: 'Line' object does not support length assignment
#>>> l3.start = 12
#Traceback (most recent call last):
#TypeError: 'start' attribute of 'Line' object supports only 'Point' object assignment
#>>> pol1 = Polygon(l1, l2, l3)
#>>> pol1.perimeter
#18.0
#>>> pol1.perimeter = 20
#AttributeError: property 'perimeter' of 'Polygon' object has no setter
#>>> l3.end = Point(-10, -10)
#>>> pol1.perimeter
#Traceback (most recent call last):
#ValueError: items doesn't form a closed polygon

