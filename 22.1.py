import os
import sys

def compareFolders2(dir1, dir2):
    files1 = set(os.listdir(dir1))
    files2 = set(os.listdir(dir2))
    dif = files1.diffference(files2)

    for item in dif:
        cur_dir = os.getcwd()
        path = os.path.join(cur_dir, item)


if __name__ == '__main__':
    res_file = input("file for result: ")
    out_res = open(res_file, "w", encoding = "utf-8")

    oldout = sys.stdout
    sys.stdout = out_res

    dir1 = input("Folder1: ")
    dir2 = input("Folder2: ")

    compareFolders2(dir1, dir2)
    out_res.close()
    sys.stdout = oldout




