from shutil import copy2
from pathlib import Path
import string
from textwrap import wrap
import shutil
from random import sample
from time import perf_counter
import sys
sys.path.append(r'C:\HW\Pautina\2024.12.14\data')
import vars


def load_file(path: Path) -> Path:

    """Функция копирует файл в текущий каталог"""

    return copy2(path, Path.cwd()/ path.name)

def remove_punctuation(text: str) -> str:

    """Функция, удаляющая знаки препинания из текста"""

    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def important_message(text: str) -> str:


    """Генерирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'"""

    size = shutil.get_terminal_size()[0]

    text = wrap(text, width = (size - 7))

    start = f"#{'=' * (size - 3)}#\n#{' ' * (size - 3)}#"
    tx = [f"#  {text[i].center(size - 7)}  #" for i in range(len(text))]
    end = f"#{' ' * (size - 3)}#\n#{'=' * (size - 3)}#"
    backslash = '\n'

    return f"{start}\n{'backslash'.join(tx)}\n{end}"


def dict_questions() -> dict[str:str]:

    """Функция, составляющая словарь с вопросами и ответами к викторине"""

    data = {}
    with open (r'C:\HW\Pautina\2024.12.14\data\questions.quiz', 'r', encoding = 'utf - 8') as questions_file:
     for line in questions_file:
      line = line.strip()
      if line == '':
       continue
      elif line.endswith('?') or line .endswith('гг'):
       question = line
       data.update({line:{}})
      else:
       data[question].update({line[3:].replace('+', '').strip():True if line.endswith('+') else False})
    return data


def user_answers(answers: list[str,str]) -> tuple[int, float]:

    """Функция, запрашивающая номер варианта ответа от пользователя и вычисляющая время ввода"""

    while True:
     start = perf_counter()
     number = input(vars.PROMPT)
     end = perf_counter()
     if not is_digit(number, answers):
      print(f"{vars.ERR_PREFIX} введите цифру номера ответа {vars.ERR_PREFIX}")
     else:
      return int(number), end - start

def is_digit(user_input: str, answers: list[str,str]) -> int| str:

    """Функция, проверяющая является ли введенное пользователем значение числом и, не превышает ли это число количество вариантов ответа"""

    if user_input.isdigit():
     num = int(user_input)
     return num if num <= len(answers) else False

def user_score(data, elem, choice_answers, number, time) -> int:

    """Функция, вычисляющая количество набранных баллов"""

    if data[elem][choice_answers[number - 1].strip()] == True and time <= vars.TIMER:
     vars.SCORE += vars.CORRECT_TIME
     print(f'Верно! {time:.1f} с')
    elif data[elem][choice_answers[number - 1]]:
     vars.SCORE += vars.CORRECT_TIMEOUT
     print(f'Верно, но недостаточно быстро. {int(time)} с')
    else:
     vars.SCORE += vars.INCORRECT
     print('Неверно...')
    return vars.SCORE

def choice_data() -> int:

    """Функция, выбирающая случайные вопросы и выводит их."""

    data = dict_questions()

    choice_questions = sample(list(data.keys()), vars.N)
    for elem in choice_questions:
      print(f"{elem}\n")
      answers = list(data[elem].keys())
      choice_answers = sample(list(data[elem].keys()), len(answers))
      for i in range(len(choice_answers)):
       print(f"{i + 1}. {choice_answers[i]}")
      number, time = user_answers(answers)
      score = user_score(data, elem, choice_answers, number, time)
      print('\n')
    return score


