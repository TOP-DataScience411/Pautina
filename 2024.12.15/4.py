from pathlib import Path
import csv

class CountableNouns:
    db_path: Path = Path(r'C:\HW\Pautina\2024.12.15\words.csv')
    words: dict[str, tuple[str, str]] = {}

    with open(db_path, 'r', encoding = 'utf-8') as csvfile:
        nouns = csv.reader(csvfile, lineterminator = '\n')
        for row in nouns:
            words[row[0]] = tuple(row[1:])

    @classmethod
    def pick(cls, number: int, word: str) -> str:

        """Принимает в качестве аргументов число и существительное для согласования в единственном числе,
        возвращает согласованное с переданным числом существительное"""

        if word in cls.words:
            if number % 10 == 1 and number != 11:
                return word
            elif (number % 10 >= 2 and number % 10 <= 4) and (number % 100 < 12 or number % 100 > 14):
                return cls.words[word][0]
            else:
                return cls.words[word][1]
        else:
            cls.save_words(word)

    @classmethod
    def save_words(cls, word1: str = None) -> None:

        """Запрашивает у пользователя два или три слова согласующихся с числительными,
        добавляет полученные значения в поле класса words и дописывает их в файл с базой существительных"""

        if word1 is None:
            word1 = input('Введите слово, согласующееся с числительным "один": ')
        word2 = input('Введите слово, согласующееся с числительным "два": ')
        word5 = input('Введите слово, согласующееся с числительным "пять": ')

        with cls.db_path.open('a', newline = '', encoding = 'utf-8') as csvfile:
            writer = csv.writer(csvfile, lineterminator = '\n')
            writer.writerow([word1] + [word2, word5])
            cls.words[word1] = tuple([word2, word5])

#>>> CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней')}
#>>> CountableNouns.pick(22, 'год')
#'года'
#>>> CountableNouns.pick(365, 'день')
#'дней'
#>>> CountableNouns.pick(21, 'попугай')
#Введите слово, согласующееся с числительным "два": попугая
#Введите слово, согласующееся с числительным "пять": попугаев
#>>> CountableNouns.words
#{'год': ('года', 'лет'), 'месяц': ('месяца', 'месяцев'), 'день': ('дня', 'дней'), 'попугай': ('попугая', 'попугаев')}
#>>> CountableNouns.save_words()
#Введите слово, согласующееся с числительным "один": капля
#Введите слово, согласующееся с числительным "два": капли
#Введите слово, согласующееся с числительным "пять": капель
#>>> print(CountableNouns.db_path.read_text(encoding='utf-8'))
#год,года,лет
#месяц,месяца,месяцев
#день,дня,дней
#попугай,попугая,попугаев
#капля,капли,капель