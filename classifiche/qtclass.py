#!/usr/bin/python2.4 

# system include
import sys, os, re, string, ConfigParser

# PyQt4 include
from PyQt4 import QtGui, QtCore

# qtclass include
from MainWin import Ui_DMainWin
from ClassDialog import Ui_ClassDialog
from RegattaDialog import Ui_RegattaDialog
from LegendaDialog import Ui_LegendaDialog
from export import Export



class MainWin(Ui_DMainWin):
    
    inputpath = ''
    outputpath = ''
    exepath = ''
    DNF = 0
    
    
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('qtclass.cfg'))
        self.exepath = config.get("path","qtclasspath")
        self.inputpath = self.exepath+config.get("path","inputpath")
        self.outputpath = self.exepath+config.get("path","outputpath")
        self.DNF = int(config.get("points", "DNF"))
        
        
    def LoadData(self):
        try:
            classes = self.ReadClasses()
        except:
            pass
        try:
            flist = os.listdir(self.inputpath)
        except:
            os.mkdir(self.inputpath)
            flist = os.listdir(self.inputpath)
        self.L_Classi.clear()
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
        
        

    def ExecClassDialog(self):
        win = QtGui.QDialog()
        uid = Ui_ClassDialog()
        uid.setupUi(win)
        if win.exec_():
            self.L_Classi.addItem(uid.T_DialogClassValue.text())
            self.WriteClasses()
            

    def ShowLegenda(self):
        win = QtGui.QDialog()
        uid = Ui_LegendaDialog()
        uid.setupUi(win)
        uid.T_Legenda.insertRow(uid.T_Legenda.rowCount())  
        pt = QtGui.QTableWidgetItem("DNF")
        pt.setTextAlignment(QtCore.Qt.AlignCenter)
        uid.T_Legenda.setItem(0,0,pt)
        pt = QtGui.QTableWidgetItem("20 points")
        pt.setTextAlignment(QtCore.Qt.AlignCenter)
        uid.T_Legenda.setItem(0,1,pt)
        win.exec_()

        
    def ExecRegattaDialog(self):
        win = QtGui.QDialog()
        uid = Ui_RegattaDialog()
        uid.setupUi(win)
        classes = self.ReadClasses()
        uid.C_RegattaClass.addItems(classes)

        if win.exec_():
            Class = uid.C_RegattaClass.currentText()
            Regatta = uid.T_DialogRegattaValue.text()
            Data = Regatta+ " " + Class 
            file = self.outputpath+re.sub(' ','_',str(Data))+".cla"
            try:
                FO = open(file, "w")
                FO.close()
                self.L_Regattas.addItem(Data)
            except:
                self.ShowErrorDialog("Error creating the file:\n%s"%file)
            
        
    def LoadClassRanking(self):
    
        if  self.T_GeneralRanking.rowCount() > 1:
            self.ClearClassRank()
        items = self.L_Classi.selectedItems()
        self.L_Classi.setCurrentItem(items[0])
        pos = self.L_Classi.currentRow()
        current_class = str(self.L_Classi.item(pos).text())
        
        regattas = os.listdir(self.inputpath)
        points = {}
        Ranks = {}            
        x = 0
        for reg in regattas:
            if re.search(current_class, reg):
                File = self.inputpath+reg
                datafile = ConfigParser.ConfigParser()
                datafile.readfp(open(File))
                for sk in datafile.options('ranking'):
                    pt = datafile.get('ranking', sk)
                    try:
                        Ranks[sk].append(pt)
                    except:
                        Ranks[sk] = [pt]
        for r in Ranks:
            tot = 0
            for pt in Ranks[r]:
                if pt == 'DNF':
                    tot = tot + self.DNF
                else:
                    tot = tot + int(pt)
            Ranks[r].append(str(tot))
            points[r] = tot
                    
        it = points.items()
        it = [(v, k) for (k, v) in it]
        it.sort()
        it = [(k, v) for (v, k) in it]
        TableHeader = ["Skipper"]
        Header = "Regatta"
        for c in range(0,len(Ranks[sk])):
            self.T_GeneralRanking.insertColumn(c+1)
            TableHeader.append("%s %d"%(Header,(c+1)))
        TableHeader.remove(TableHeader[len(TableHeader)-1])
        TableHeader.append("Tot")
        self.T_GeneralRanking.setHorizontalHeaderLabels(TableHeader)     
        for sk_ in it:
            sk = sk_[0]
            self.T_GeneralRanking.insertRow(self.T_GeneralRanking.rowCount())  
            ski = QtGui.QTableWidgetItem(sk)
            self.T_GeneralRanking.setItem(x,0,ski)
            c = 1
            for p in Ranks[sk]:
                if p == '999':
                    p = 'DNF'
                pt = QtGui.QTableWidgetItem(p)
                pt.setTextAlignment(QtCore.Qt.AlignCenter)
                self.T_GeneralRanking.setItem(x,c,pt)
                c = c + 1
            x = x + 1
        self.T_GeneralRanking.resizeColumnsToContents()    

    def LoadRegattaRanking(self):
        current_class = ''
        if self.T_DetailRanking.rowCount() > 1:
            self.ClearRankTable()
        for c in range(0, self.L_Regattas.count()):
            if self.L_Regattas.isItemSelected(self.L_Regattas.item(c)) == True:
                current_class = self.L_Regattas.item(c).text()
                break
        if current_class != '':
            File = self.inputpath+re.sub(' ','_',str(current_class))+".cla"
            Header = "Race"
            
            try:
                datafile = ConfigParser.ConfigParser()
                datafile.readfp(open(File))
            except:
                return
  
            x = 0
            TableHeader = ["Skipper"]
            points = {}
            Ranks = {}            
            for sk in datafile.options('result'):
                _pt = datafile.get('result', sk)
                pt = _pt.split(',')
                tot = 0
                Ranks[sk] = pt
                for p in pt:
                    if p == 'DNF':
                        tot = tot + self.DNF
                    else:
                        tot = tot + int(p)
                Ranks[sk].append(str(tot))
                points[sk] = tot
            it = points.items()
            it = [(v, k) for (k, v) in it]
            it.sort()
            it = [(k, v) for (v, k) in it]
            for c in range(0,len(Ranks[sk])):
                self.T_DetailRanking.insertColumn(c+1)
                TableHeader.append("%s %d"%(Header,(c+1)))
            TableHeader.remove(TableHeader[len(TableHeader)-1])
            TableHeader.append("Tot")
            self.T_DetailRanking.setHorizontalHeaderLabels(TableHeader)     
            for sk_ in it:
                sk = sk_[0]
                self.T_DetailRanking.insertRow(self.T_DetailRanking.rowCount())  
                ski = QtGui.QTableWidgetItem(sk)
                self.T_DetailRanking.setItem(x,0,ski)
                c = 1
                for p in Ranks[sk]:
                    if p == '999':
                        p = 'DNF'
                    pt = QtGui.QTableWidgetItem(p)
                    pt.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.T_DetailRanking.setItem(x,c,pt)
                    c = c + 1
                x = x + 1
            self.T_DetailRanking.resizeColumnsToContents()    
        
    
    def ClearRankTable(self):
        self.ClearTable(self.T_DetailRanking)
        self.T_DetailRanking.setHorizontalHeaderLabels(["Skipper"])
        
    def ClearClassRank(self):
        self.ClearTable(self.T_GeneralRanking)
        self.T_GeneralRanking.setHorizontalHeaderLabels(["Skipper"])   
                        
    def ClearTable(self, Item):
        Item.clear()
        Item.setRowCount = 0
        Item.setColumnCount = 0
        rows = Item.rowCount()
        cols = Item.columnCount()
        for i in range(cols, 0, -1):
            Item.removeColumn(i)
        for i in range(rows, 0, -1):
            Item.removeRow(i)
        Item.removeRow(0)
        Item.setRowCount = 0
        Item.setColumnCount = 0
              
        
    def AddSkipper(self):
        self.T_DetailRanking.insertRow(self.T_DetailRanking.rowCount())
        
    def AddRace(self):
        self.T_DetailRanking.insertColumn(self.T_DetailRanking.columnCount()-1)
        cols = self.T_DetailRanking.columnCount()
        if cols == 2:
            self.T_DetailRanking.insertColumn(self.T_DetailRanking.columnCount()-1)
            cols += 1
        TableHeader=[]
        for c in range(0, cols -1):
            TableHeader.append("%s %d"%("Race",(c)))
        TableHeader[0] = "Skipper"
        TableHeader.append("Tot")
        self.T_DetailRanking.setHorizontalHeaderLabels(TableHeader)  
        self.T_DetailRanking.resizeColumnsToContents() 
        
        
    def SaveRankingData(self):
        datafile = ConfigParser.ConfigParser()
        datafile.add_section('result')
        if self.L_Regattas.currentItem() == None:
            self.ShowWarningDialog("Please select a regatta.\n")
            return
        current_regatta = self.L_Regattas.currentItem().text()
        fname = self.outputpath+re.sub(' ','_',str(current_regatta))+".cla"
        FO = open(fname, "w")
        datafile.readfp(FO)
        rows = self.T_DetailRanking.rowCount()
        cols = self.T_DetailRanking.columnCount()
        for row in range (0, rows):
            skipper = str(self.T_DetailRanking.item(row,0).text())
            races = []
            for x in range(1, cols -1):
                races.append(str(self.T_DetailRanking.item(row,x).text()))
            opt = skipper
            value = ",".join(races)
            datafile.set('result',opt, value)
        datafile.add_section('ranking')
        points = {}
        for row in range(0, rows):
            opt = str(self.T_DetailRanking.item(row,0).text())
            value = str(self.T_DetailRanking.item(row,cols-1).text())
            points[opt] = int(value)
        it = points.items()
        it = [(v, k) for (k, v) in it]
        it.sort()
        it = [(k, v) for (v, k) in it]
        c = 1
        for i in it:
            datafile.set('ranking',str(i[0]), str(c))
            c += 1
        datafile.write(FO)
        FO.close()
        self.ShowMessageDialog("File %s saved"%fname)
            
    def CheckRegatta(self):
        if self.L_Regattas.currentItem() == None:
            self.ShowWarningDialog("Please select a regatta.\n")
            return
            
    def ShowMessageDialog(self, msg):
        QtGui.QMessageBox.information(None, self.tr("Info"),
                        self.tr(msg),
                        QtGui.QMessageBox.Ok )
    
    def ShowWarningDialog(self, msg):
        QtGui.QMessageBox.warning(None, self.tr("Alert"),
                        self.tr(msg),
                        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                        QtGui.QMessageBox.Escape)
    
    def ShowErrorDialog(self, msg):
        QtGui.QMessageBox.critical(None, self.tr("Error"),
                        self.tr(msg),
                        QtGui.QMessageBox.Ok | QtGui.QMessageBox.Default,
                        QtGui.QMessageBox.Escape)
   
    def UpdateRegattaRanking(self):
        rows = self.T_DetailRanking.rowCount()
        cols = self.T_DetailRanking.columnCount()
        for row in range(0,rows):
            tot = 0
            for col in range(1, cols-1):
                tot += int(self.T_DetailRanking.item(row, col).text())
            tot = QtGui.QTableWidgetItem(str(tot))
            self.T_DetailRanking.setItem(row,col+1,tot)
            
    
    def CancelRace(self):
        x = self.T_DetailRanking.currentColumn()
        # Check if is the column of the totals
        if x == self.T_DetailRanking.columnCount() - 1:
            self.ShowWarningDialog("You cannot delete the total.")
            return
        self.T_DetailRanking.removeColumn(x)
        
    def CancelSkipper(self):
        self.T_DetailRanking.removeRow(self.T_DetailRanking.currentRow())
        
    def ExportRanking(self, DataType, DataSource):
        if DataType.currentItem() == None:
            self.ShowWarningDialog("Please select a regatta.\n")
            return
        regatta = DataType.currentItem().text()
        
        fileType = QtCore.QString("pdf *.pdf")
        fileName = QtGui.QFileDialog.getSaveFileName(None,"Save As...",
                                                            "./export",
                                                            "pdf (*.pdf);;html (*.html);;blg (*.blg)",
                                                            fileType
                                                            )
        FileExt = ".pdf"
        ext = str(fileType).split(" ")
        ExportEngine = Export()
        if ext[0] == "html":
            FileExt = ".html"
            if fileName[-5:] == FileExt:
                FileExt = ""
            fname = fileName+FileExt
            ExportEngine.ExportAsHTML(DataSource, fname, regatta)
        if ext[0] == "pdf":
            FileExt = ".pdf"
            if fileName[-4:] == FileExt:
                FileExt = ""
            fname = fileName+FileExt
            ExportEngine.ExportAsPDF(DataSource, fname, regatta)
        if ext[0] == "blg":
            FileExt = ".blg"
            if fileName[-4:] == FileExt:
                FileExt = ""
            fname = fileName+FileExt
            ExportEngine.ExportAsBLG(DataSource, fname, regatta)
        
    
    def ExportClassRank(self):
        self.ExportRanking(self.L_Classi, self.T_GeneralRanking)
        
    
    def ExportRegattaRank(self):
        self.ExportRanking(self.L_Regattas, self.T_DetailRanking)
    

    def CancelClass(self):
        row = self.L_Classi.currentRow()
        i = self.L_Classi.takeItem(row)
        del i
        self.WriteClasses()
    
    def CancelRegatta(self):
        row = self.L_Regattas.currentRow()
        i = self.L_Regattas.takeItem(row)
        current_reg=i.text()
        file = self.inputpath+re.sub(' ','_',str(current_reg))+".cla"
        os.remove(file)
        del i
            
    def CheckData(self):
        if self.T_DetailRanking.currentItem() == None:
            return
        print "---",self.T_DetailRanking.currentColumn()

        if self.T_DetailRanking.currentColumn() == 0:
            #check for skipper
            return
        print "Here"
        if self.T_DetailRanking.currentColumn() > 0:
            if self.CheckIfInt(self.T_DetailRanking.currentItem().text()) == 0:
                self.ShowErrorDialog("Points must be a number")
                return
                
            
    
    def CheckIfInt(self, value):
        ok = 1
        try:
            num = int(value)
            print num
        except ValueError:
            ok = 0
        print ok
        return ok            
    # End of Class



app = QtGui.QApplication(sys.argv)
window = QtGui.QDialog()
ui = MainWin()
ui.setupUi(window)

# Custom Signal connections
QtCore.QObject.connect(ui.B_AddClass, QtCore.SIGNAL("clicked()"), ui.ExecClassDialog)
QtCore.QObject.connect(ui.B_AddRegatta, QtCore.SIGNAL("clicked()"), ui.ExecRegattaDialog)
QtCore.QObject.connect(ui.L_Classi, QtCore.SIGNAL("itemSelectionChanged()"), ui.LoadClassRanking)
QtCore.QObject.connect(ui.L_Regattas, QtCore.SIGNAL("itemSelectionChanged()"), ui.LoadRegattaRanking)
QtCore.QObject.connect(ui.B_AddSkipper, QtCore.SIGNAL("clicked()"), ui.AddSkipper)
QtCore.QObject.connect(ui.B_AddRace, QtCore.SIGNAL("clicked()"), ui.AddRace)
QtCore.QObject.connect(ui.T_DetailRanking, QtCore.SIGNAL("itemSelectionChanged()"), ui.CheckRegatta)
QtCore.QObject.connect(ui.T_DetailRanking, QtCore.SIGNAL("itemChanged(QTableWidgetItem *)"), ui.CheckData)
QtCore.QObject.connect(ui.B_Legenda, QtCore.SIGNAL("clicked()"), ui.ShowLegenda)
QtCore.QObject.connect(ui.B_CalcRanking, QtCore.SIGNAL("clicked()"), ui.UpdateRegattaRanking)
QtCore.QObject.connect(ui.B_DeleteSkipper, QtCore.SIGNAL("clicked()"), ui.CancelSkipper)
QtCore.QObject.connect(ui.B_DeleteRace, QtCore.SIGNAL("clicked()"), ui.CancelRace)
QtCore.QObject.connect(ui.B_SaveRegattaRank, QtCore.SIGNAL("clicked()"), ui.SaveRankingData)
QtCore.QObject.connect(ui.B_ExportClassRank, QtCore.SIGNAL("clicked()"), ui.ExportClassRank)
QtCore.QObject.connect(ui.B_ExportRegattaRank, QtCore.SIGNAL("clicked()"), ui.ExportRegattaRank)
QtCore.QObject.connect(ui.B_CancelClass, QtCore.SIGNAL("clicked()"), ui.CancelClass)
QtCore.QObject.connect(ui.B_CancelRegatta, QtCore.SIGNAL("clicked()"), ui.CancelRegatta)

ui.LoadData()
window.show()
sys.exit(app.exec_())


