#!/usr/bin/env python


class QtRankingIO:
    def __init__(self):
        pass
    
    def LoadData(self):
        try:
            classes = self.ReadClasses()
        except:
            pass
        try:
            flist = os.listdir('./saved_data')
        except:
            os.mkdir(self.inputpath)
            flist = os.listdir('./saved_data')
        self.CB_Classes.clear()
        self.L_Regattas.clear()
        self.L_Classi.addItems(classes)
        for cl in flist:
            try:
                p = cl.rindex('_') + 1
                if cl[p:-4] in (classes):
                    Regatta = re.sub('_',' ',cl[:-4])
                    self.L_Regattas.addItem(Regatta)
            except:
                pass
    
        def ReadClasses(self):
            FI = open("./data/classes","r")
            cla = FI.read()
            FI.close()
            classes = []
            _classes = cla.split("\n")
            for c in _classes:
                # -FIXME-
                # To delete the \r in case we are using a win* platform
                # must find a better method anyway
                if c[-1:] == '\r':
                    c = c[:-1]
                if c != '':
                    classes.append(c)
            return classes
            
        def WriteClasses(self):
            FO = open("./data/classes","w")
            r = self.L_Classi.count()
            for c in range(0,r):
                FO.write(self.L_Classi.item(c).text())
                FO.write("\n")
            FO.close()
