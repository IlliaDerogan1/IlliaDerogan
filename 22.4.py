import os
import sys



def archive(folder, date_now):
    files = os.listdir()
    for it in file:
        if os.path.isfile(it) and it.endwith(".log"):
            path = os.path.join(os.getcwd(), it)
            time1 = os.path.getmtime(path)
            if time1 < date_now:
                lst.append(path)

    if lst:
        arch_file = os.path.join(os.getcwd(), date_now.strftime("%Y%m%d%H%M%S") + ".tar.gz")
        with tarfile.open(arch_file, "w:gz") as tf:
            for it in lst:
                tf.add(it)
                os.remmove(path)

if __name__ == '__main__':
    date_now = datetime.datetime.now()
    folder = input("Folder ")
    archive(folder, date_now)
