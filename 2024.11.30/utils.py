from textwrap import wrap
import shutil

def important_message(text: str) -> str:

    """Генирирует строку, в которой переданный текст будет обрамлён рамкой из символов '=' и '#'"""

    size = shutil.get_terminal_size()[0]

    text = wrap(text, width = (size - 7))


    start = f"#{'=' * (size - 3)}#\n#{' ' * (size - 3)}#"
    tx = [f"#  {text[i].center(size - 7)}  #" for i in range(len(text))]
    end = f"#{' ' * (size - 3)}#\n#{'=' * (size - 3)}#"
    
    return f"{start}\n{'\n'.join(tx)}\n{end}"





