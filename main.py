import sys
import argparse
import os
import algoritms

choice_func = {
    1: algoritms.file_dfs,
    2: algoritms.file_bfs,
    3: algoritms.file_datefs,
}


def validate_path(path):
    if os.path.isdir(path):
        if os.access(path, os.X_OK):
            return path
    raise argparse.ArgumentTypeError(f"No dir with path {path} or no access ")


def get_parser():
    parser = argparse.ArgumentParser(description='''Скрипт для тестового задания''', )
    parser.add_argument("-a", "--algorithm", choices=[1, 2, 3], type=int,
                        help="Bыбор алгоритма \n \n1: Обход в глубину "
                             "\n\t2: Обход в ширину \n\t3: Обход в глубину со срезами по дате")
    parser.add_argument("-p", "--path", type=validate_path, help="Выбор дериктории")
    parser.add_argument("-ns", "--need_sort_by_name", type=int, choices=[0, 1], default=0,
                        help="Сортировать названия дерикторий в лексикографическом порядке ")
    return parser


def main():
    # print(sys.argv)
    parser = get_parser()
    namespace = parser.parse_args(sys.argv[1:])
    # print("^" * 100)
    # print(namespace)
    choice_func[namespace.algorithm](namespace.path, namespace.need_sort_by_name)


if __name__ == '__main__':
    main()
