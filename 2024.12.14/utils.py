from shutil import copy2
from pathlib import Path
import string


def load_file(path: Path) -> Path:

	"""Функция копирует файл в текущий каталог"""

	return copy2(path, Path.cwd()/ path.name)


    
def remove_punctuation(text: str) -> str:

	"""Функция, удалающая знаки препинания из текста"""

	translator = str.maketrans('', '', string.punctuation)
	return text.translate(translator)
