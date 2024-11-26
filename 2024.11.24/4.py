from random import randrange

tree = []

def tree_generation(size: int = randrange(1, 10)) -> list:
    """
    Функция, генерирующая дерево с произвольным количеством веток и листьев.
    Необязательный параметр функции size, принимает случайное значение, влияет на количество веток.
    """
    branch = []
    if size == 0 and len(tree) != 0:
        return tree
    else:
        for _ in range(randrange(10)):
            branch.append('leaf')
        tree.append(branch)
        return tree_generation(size - 1)
        
    
    return tree
    
#>>> tree_generation()
#[['leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], ['leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf']]
#>>> tree_generation()
#[['leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], ['leaf'], ['leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], [], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], []]


