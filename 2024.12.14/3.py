from pathlib import Path
from utils import load_file
from importlib.util import spec_from_file_location, module_from_spec

def ask_for_file():
  while True:
    path_for_file = Path(input('Введите путь к файлу:\n'))
    if path_for_file.exists() == False:
      print('По указанному пути файла не существует.\nВведите корректный путь:\n')
      continue
    else:
      break
  copy_file = load_file(path_for_file)

  spec = spec_from_file_location("conf.py", path_for_file)
  module = module_from_spec(spec)
  spec.loader.exec_module(module)
  return module


#>>> config_module = ask_for_file()
#Введите путь к файлу:
#d:\student\2023.05.28\conf.py
#По указанному пути файла не существует.
#Введите корректный путь:
#
#Введите путь к файлу:
#C:\Users\Яна\Pautina\2024.12.14\data\conf.py
#>>>
#>>> config_module.defaults
#{'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
