tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]

def tree_leaves(tree: list[int]) -> int:
    """
    Функция, считающая количество листьев на дереве.
    считает количество листьев на дереве. 
    Принимает обязательным позиционно-ключевым аргументом список веток дерева.
    """
    cnt = 0
    for elem in tree:
        if isinstance(elem, list):
            banrch = tree_leaves(elem)
            cnt += banrch
        else:
            cnt += 1
    return cnt
    
#>>> tree_leaves(tree)
#38
