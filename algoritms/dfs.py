import os
from typing import Set, List
from .utils import print_file_info


def file_dfs(start: str, need_sort_by_name: bool = False) -> None:
    """
    Обход в глубину дериктории
    :param start: начальная дериктория
    :param need_sort_by_name: сортировать названия папок в лексикографическом порядке
    """
    try:
        os.path.isdir(start)
    except FileNotFoundError as e:
        print(f"Can't find folder with path {start}")

    file_dfs_util(start, set(), [], need_sort_by_name)


def file_dfs_util(start: str, visited: Set[str], stack: List[str], need_sort_by_name: bool = False) -> None:
    """
    :param start: текушая дериктория
    :param visited: множество уже посещенных дерикторий (множество что бы проверка наличия элемента работала за О(1))
    :param stack:  хранит абсолютные пути
    :param need_sort_by_name: сортировать названия папок в лексикографическом порядке
    :return:
    """
    os.chdir(start)
    fnf = os.listdir()
    visited.add(start)
    if need_sort_by_name:
        fnf = sorted(fnf, reverse=True)

    for elem in fnf:
        if os.path.isfile(elem):
            print_file_info(elem)
        else:
            stack.append(f"{os.getcwd()}/{elem}")
    while stack:
        start = stack.pop()
        if start in visited:
            continue
        file_dfs_util(start, visited, stack)


# file_dfs("/home/andreyvaran/pythonProject/Test_task_to_spetsvuz/A", need_sort_by_name=True)
