class OpenFile:
    def __init__(self,filename):
        self.filename = filename
        self.p = str()
    def set_p(self):
        self.p = (i==0 and self.p + self.filename.split('/')[i]) or (i!=0 and self.p + '/' + self.filename.split('/')[i])
    def get_path(self):
        k = len(self.filename.split('/'))
        for i in range(0, k - 1):
            self.p = (i==0 and self.p + self.filename.split('/')[i]) or (i!=0 and self.p + '/' + self.filename.split('/')[i])
        return self.p

#        for e in lst:  func(e)
#        map(func,lst)

newfile = OpenFile('C:/drawing/cad/tabelle fori XYZ/Hole Table Generator/sorgenti/filetestarea/test.vda')
print(newfile.get_path())
