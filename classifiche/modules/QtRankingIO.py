#!/usr/bin/env python

import os, re, string, ConfigParser

class QtRankingIO:
    
    Classes = []
    Regattas = {}
    def __init__(self):
        pass
    
    def LoadData(self, gui):
        try:
            flist = os.listdir('./saved_data')
        except:
            os.mkdir(gui.inputpath)
            flist = os.listdir('./saved_data')
        gui.CB_Regattas.clear()
        gui.CB_Regattas.addItem('')
        for cl in flist:
            try:
                p = cl.rindex('_') + 1
                Regatta = re.sub('_',' ',cl[:-4])
                gui.CB_Regattas.addItem(Regatta)
            except Exception, e:
                print e
    
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
        r = gui.L_Classi.count()
        for c in range(0,r):
            FO.write(gui.CB_Classi.item(c).text())
            FO.write("\n")
        FO.close()

        
    def LoadRegattaRanking(self, data, rank):
        res = {}
        datafile = ConfigParser.ConfigParser()
        datafile.readfp(open(data))
        section_to_read = 'result_'+str(rank)
        for sk in datafile.options(section_to_read):
            res[sk] = datafile.get(section_to_read, sk).split(',')
        return res
            
