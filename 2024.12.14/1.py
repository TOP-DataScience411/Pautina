from pathlib import Path

def list_files(absolutepath: str) -> tuple(str):
	pathdate = Path(absolutepath)
	return tuple([file.name for file in pathdate.iterdir() if file.is_file()])


#list_files(r'C:\data scientist\Pautina\2024.12.14\data')
#('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')


