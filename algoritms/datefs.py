from datetime import datetime
from dateutil.relativedelta import relativedelta
from .utils import print_file_info, DatetimeRange
import os

from typing import Set, List

temp = datetime.now()
date_dict = {
    DatetimeRange(temp - relativedelta(months=1), temp): "0 month",
    DatetimeRange(temp - relativedelta(months=2), temp - relativedelta(months=1)): "1 months",
    DatetimeRange(temp - relativedelta(months=3), temp - relativedelta(months=2)): "2 months",
    DatetimeRange(temp - relativedelta(months=4), temp - relativedelta(months=3)): "3 months",
    DatetimeRange(temp - relativedelta(months=5), temp - relativedelta(months=4)): "4 months",
    DatetimeRange(temp - relativedelta(months=6), temp - relativedelta(months=5)): "5 months",
    DatetimeRange(temp - relativedelta(months=7), temp - relativedelta(months=6)): "6 months",
    DatetimeRange(temp - relativedelta(months=8), temp - relativedelta(months=7)): "7 months",
    DatetimeRange(temp - relativedelta(months=9), temp - relativedelta(months=8)): "8 months",
    DatetimeRange(temp - relativedelta(months=10), temp - relativedelta(months=9)): "9 months",
    DatetimeRange(temp - relativedelta(months=11), temp - relativedelta(months=10)): "10 months",
    DatetimeRange(temp - relativedelta(months=12), temp - relativedelta(months=11)): "11 months",
    DatetimeRange(temp - relativedelta(months=600), temp - relativedelta(months=12)): "1 year ",
}


def file_datefs(start: str, need_sort_by_name: bool = False) -> None:
    """
    Обход в глубину дериктории
    :param start: начальная дериктория
    :param need_sort_by_name: сортировать названия папок в лексикографическом порядке
    """
    try:
        os.path.exists(start)
    except FileNotFoundError as e:
        print(f"Can't find folder with path {start}")

    start_dir_path = f"{os.getcwd()}" if not os.path.isabs(start) else start
    for key in date_dict.keys():
        file_datefs_util(f"{start}", set(), [], key, False, need_sort_by_name)
        os.chdir(start_dir_path)


def file_datefs_util(start: str, visited: Set[str], stack: List[str],
                     date_range: DatetimeRange, printed: bool, need_sort_by_name: bool = False) -> None:
    """
    :param printed:
    :param date_range:
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
            if (datetime.fromtimestamp(os.path.getctime(elem)) in date_range):
                if not printed:
                    print(f"older than {date_dict[date_range]}")
                    printed = True
                print_file_info(elem)
        else:
            stack.append(f"{os.getcwd()}/{elem}")
    while stack:
        start = stack.pop()
        if start in visited:
            continue
        file_datefs_util(start, visited, stack, date_range, printed)

# print(date_dict)
# file_datefs("Test_task_to_spetsvuz/A", True)
