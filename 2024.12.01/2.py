from urllib.request import urlopen
from re import findall, S
from json import dump
from pathlib import Path
from chardet import detect

def json_from_html(url: str, pattern: str, encoding: str = 'utf-8') -> Path:

    with urlopen(url) as response:
        html_bytes = response.read()
    
    encoding = detect(html_bytes)['encoding']

    html = html_bytes.decode(encoding)
    
    matches = findall(pattern, html, S)
    matches_dict = {match[0] : match[1] for match in matches}
    
    if url.endswith('.html'):
        json_filename = Path(url).name.replace('.html', '.json')
    else:
        json_filename = f"{Path(__loader__.path).stem}.json"
    
    json_path = Path(json_filename)
    
    with json_path.open('w', encoding='utf-8') as jsonfile:
        dump(matches_dict, jsonfile, ensure_ascii=False, indent=2)
    
    return json_path


url = 'http://www.world-art.ru/cinema/rating_top.php'
films_pattern = (r'<tr .*?>'
r'<td .*?<a.*?>(?P<name>.*?)</a>.*?</td>'
r'<td .*?>(?P<rating>.*?)</td>')

file_path = json_from_html(url, films_pattern)
print(file_path.name)
print(file_path.read_text(encoding='utf-8')[:110])



url = 'https://docs.python.org/3/py-modindex.html'
modules_pattern = r'<tr>.+?>(\w+?)<.+?</td><td>.*?<em>(.*?)</em>'
file_path = json_from_html(url, modules_pattern)
print(file_path.name)
print(file_path.read_text(encoding='utf-8')[:110])


