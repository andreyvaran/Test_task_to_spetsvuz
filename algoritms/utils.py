import hashlib
import os
from datetime import datetime


def print_file_info(filename: str) -> None:
    with open(filename, "rb") as file:
        md5_hash = hashlib.md5()
        md5_hash.update(file.read())
        result = md5_hash.hexdigest()
        print(
            f"{result} {os.path.getsize(filename) : 6d} {datetime.fromtimestamp(os.path.getctime(filename)).strftime('%Y-%m-%d %H:%M')} {os.path.abspath(filename)}")


class DatetimeRange:
    def __init__(self, dt1, dt2):
        self._dt1 = dt1
        self._dt2 = dt2

    def __contains__(self, dt):
        return self._dt1 < dt < self._dt2
