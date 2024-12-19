from shutil import copy2
from sys import path
from pathlib import Path


def load_file(path: Path) -> Path:

	"""Функция копирует файл в текущий каталог"""

    return copy2(path, Path.cwd()/ path.name)



