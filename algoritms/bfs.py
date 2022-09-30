from collections import deque

from .utils import print_file_info
import os
from typing import Set, Deque


def file_bfs(start: str, need_sort_by_name: bool = False) -> None:
    """
    Обход в ширину для дериктории
    :param start: начальная дериктория
    :param need_sort_by_name: сортировать ли в лексикографическом порядке
    """
    try:
        os.path.isdir(start)
    except FileNotFoundError as e:
        print(f"Can't find folder with path {start}")

    file_bfs_util(start, set(), deque([start]), need_sort_by_name)


def file_bfs_util(start: str, visited: Set[str], queue: Deque[str], need_sort_by_name: bool = False) -> None:
    """

    :param start: текушая дериктория
    :param visited: множество уже посещенных дерикторий (множество что бы проверка наличия элемента работала за О(1))
    :param queue: Очередь в которую мы записываем вершины в которые должны зайти
    :param need_sort_by_name: сортировать ли в лексикографическом порядке
    """
    os.chdir(start)
    fnf = os.listdir()
    visited.add(start)
    need_go_up = True
    if need_sort_by_name:
        fnf = sorted(fnf, reverse=True)

    for elem in fnf:
        if os.path.isfile(elem):
            print_file_info(elem)
        else:
            queue.append(f"{os.getcwd()}/{elem}")
    if need_go_up:
        os.chdir("..")

    while queue:
        start = queue.popleft()
        if start in visited:
            continue
        file_bfs_util(start, visited, queue)


# print(os.getcwd())
# file_bfs("/home/andreyvaran/pythonProject/", need_sort_by_name=True)
