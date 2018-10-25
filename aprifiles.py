from tkinter import filedialog
import os


class ReturnFile(object):
    def __init__(self, p, f, in_file):
        self.p = p
        self.in_file = in_file
        self.f = f


def apri_file_diag():
    return filedialog.askopenfilename(initialdir="C:\\", title="Seleziona vda",
                                      filetypes=(("File vda", "*.vda"), ("all files", "*.*")))


def aprivda(filename):
    if filename:
        path = filename
        name = path.split('/')
        k = len(name)
        f = name[k - 1]
        f = f.strip("vda")
        p = ""
        for i in range(0, k - 1):
            if i == 0:
                p = p + name[i]
            else:
                p = p + '/' + name[i]
        try:
            os.chdir(p)
        except OSError:
            p = 0
            f = 0
            in_file = 0
            return ReturnFile(p, f, in_file)
        else:
            try:
                in_file = open(filename, "r")
            except OSError:
                p = 0
                f = 0
                in_file = 0
                return ReturnFile(p, f, in_file)
            else:
                return ReturnFile(p, f, in_file)
    else:
        p = 0
        f = 0
        in_file = 0
        return ReturnFile(p, f, in_file)