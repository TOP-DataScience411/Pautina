class ChessKing:
    ranks: dict[str, int] = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8}
    files: dict[str, int] = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

    def __init__(self, color: str = None, square: str = None):
        self.color = color
        self.square = square
        if None == self.color:
            self.color = 'white'
        if None == self.square:
            if self.color == 'white':
                self.square = 'e1'
            else:
                self.square = 'e8'

    def __repr__(self) -> str:

        """Возвращает машиночитаемое строковое представление"""

        return f"'{self.color[0].upper()}K: {self.square}'"

    def __str__(self) -> str:

        """Возвращает человекочитаемое строковое представление"""

        return f'{self.color[0].upper()}K: {self.square}'

    def is_turn_valid(self, new_square: str) -> bool:

        """Принимает на вход строку нового поля и проверяет, возможен ли для данной фигуры ход с текущего поля на новое"""

        return (-1 <= (self.files[self.square[0]] + 1) -
                (self.files[new_square[0]] + 1) <= 1 and
                -1 <= (self.ranks[self.square[1]] + 1) -
                (self.ranks[new_square[1]] + 1) <= 1
                )

    def turn(self, new_square: str) -> None:

        """Принимает на вход строку нового поля и выполняет ход, выбрасывает ValueError в случае невозможности выполнить ход"""
        
        if self.is_turn_valid(new_square):
            self.square = new_square
        else:
            raise ValueError('Невозможно выполнить ход')


#>>> wk = ChessKing()
#>>> wk.color
#'white'
#>>> wk.square
#'e1'
#>>> wk.turn('e2')
#>>> wk
#'WK: e2'
#>>> wk.turn('d4')
#    raise ValueError('Невозможно выполнить ход')
#ValueError: Невозможно выполнить ход
#>>> bk = ChessKing('black')
#>>> print(bk)
#BK: e8