import os
from random import randint


def some_data_to_file(filename: str):
    with open(filename, "w") as f:
        for i in range(randint(1, 10)):
            f.write("hello world " * randint(20, 100) + "\n")


os.system("mkdir A")
os.chdir("A")
os.system("mkdir C")
os.system(
    "> somefile1.txt")
os.system(
    "> somefile2.txt")
some_data_to_file("somefile1.txt")
some_data_to_file("somefile2.txt")
os.system("mkdir B")
os.chdir("B")
os.system("mkdir D")
os.system(
    "> fileinb.txt")
os.system(
    "> fileinb2.txt")
os.system(
    "> fileinb3.txt")
os.system(
    "> fileinb4.txt")
some_data_to_file("fileinb.txt")
some_data_to_file("fileinb2.txt")
some_data_to_file("fileinb3.txt")
some_data_to_file("fileinb4.txt")
os.chdir("D")
os.system(
    "> dfile.txt")
os.system(
    "> dfilesuper.txt")
os.system(
    "> dfile3.txt")
some_data_to_file("dfile.txt")
some_data_to_file("dfilesuper.txt")
some_data_to_file("dfile3.txt")
os.chdir("..")
os.chdir("..")
os.chdir("C")
os.system(
    "> cfile.txt")
os.system(
    "> cfile1.txt")
os.system(
    "> cfile2.txt")
some_data_to_file("cfile.txt")
some_data_to_file("cfile1.txt")
some_data_to_file("cfile2.txt")
