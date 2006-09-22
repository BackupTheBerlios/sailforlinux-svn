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
                    print Regatta
                    self.L_Regattas.addItem(Regatta)
            except:
                print "Here"
        
    def ReadClasses(self):
        FI = open("./data/classes","r")
        cla = FI.read()
        FI.close()
        classes = cla.split("\n")
        return classes
                    
    def ExecClassDialog(self):
        win = QtGui.QDialog()
        uid = Ui_ClassDialog()
        uid.setupUi(win)
        if win.exec_():
            self.L_Classi.addItem(uid.T_DialogClassValue.text())

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
            Class = uid.T_DialogClassValue.text()
            Regatta = uid.T_DialogRegattaValue.text()
            Data = Regatta+ " " + Class 
            file = self.outputpath+re.sub(' ','_',str(Data))+".cla"
            try:
                FO = open(file, "w")
                FO.close()
                self.L_Regattas.addItem(Data)
            except:
                self.ShowErrorDialog("Error creating the file:\n%s"%file)
            self.SetRankingTable(uid.T_DialogSkipperValue.text(),
                                    uid.T_DialogRaceValue.text())

    def SetRankingTable(self, skipper, race):
        TableHeader = ["Skipper"]
        for x in range (0,int(skipper)):
            self.T_DetailRanking.insertRow(self.T_DetailRanking.rowCount())
            TableHeader.append("Race %d"%(x+1))
        for y in range(0,int(race)):
            self.T_DetailRanking.insertColumn(self.T_DetailRanking.columnCount())
        self.T_DetailRanking.setHorizontalHeaderLabels(TableHeader)    
        
    def LoadClassRanking(self):
        if  self.T_GeneralRanking.rowCount() > 1:
            self.ClearClassRank()
        items = self.L_Classi.selectedItems()
        self.L_Classi.setCurrentItem(items[0])
        pos = self.L_Classi.currentRow()
        current_class = self.L_Classi.item(pos).text()
        file = self.inputpath+"generale_%s_2006.cla"%current_class
        self.LoadDataFile(file, self.T_GeneralRanking, "Reg.")

    def LoadRegattaRanking(self):
        current_class = ''
        if self.T_DetailRanking.rowCount() > 1:
            self.ClearRankTable()
        for c in range(0, self.L_Regattas.count()):
            if self.L_Regattas.isItemSelected(self.L_Regattas.item(c)) == True:
                current_class = self.L_Regattas.item(c).text()
                break
        if current_class != '':
            file = self.inputpath+re.sub(' ','_',str(current_class))+".cla"
            self.LoadDataFile(file, self.T_DetailRanking, "Race")
       
        
    def LoadDataFile(self, File, Item, Header):
        try:
            FI = open(File, 'r')
            _LRank = FI.read()
            FI.close()
        except:
            return

        LRank = _LRank.replace("\r","")
        Rank = LRank.split('\n')
        Ranks = {}
        x = 0
        TableHeader = ["Skipper"]
        for cr in Rank:
            if cr == '':
                break
            sk = cr[0:cr.index('=')]
            Ranks[sk] = cr[cr.index('=')+1:].split(',')
        points = {}
        for sk in Ranks:
            tot = 0    
            for p in Ranks[sk]:
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
            Item.insertColumn(c+1)
            TableHeader.append("%s %d"%(Header,(c+1)))
        TableHeader.remove(TableHeader[len(TableHeader)-1])
        TableHeader.append("Tot")
        Item.setHorizontalHeaderLabels(TableHeader)     
        y = 0
        for sk_ in it:
            sk = sk_[0]
            Item.insertRow(Item.rowCount())  
            ski = QtGui.QTableWidgetItem(sk)
            Item.setItem(x,0,ski)
            c = 1
            for p in Ranks[sk]:
                if p == '999':
                    p = 'DNF'
                pt = QtGui.QTableWidgetItem(p)
                pt.setTextAlignment(QtCore.Qt.AlignCenter)
                Item.setItem(x,c,pt)
                c = c + 1
            x = x + 1
        Item.resizeColumnsToContents()    
        
    
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
        TableHeader=[]
        for c in range(0,self.T_DetailRanking.columnCount()-1):
            TableHeader.append("%s %d"%("Race",(c)))
        TableHeader[0] = "Skipper"
        TableHeader.append("Tot")
        self.T_DetailRanking.setHorizontalHeaderLabels(TableHeader)  
        self.T_DetailRanking.resizeColumnsToContents() 
        
        
    def SaveRankingData(self, DataType, DataSource):
        if DataType.currentItem() == None:
            self.ShowWarningDialog("Please select a regatta.\n")
            return
        current_regatta = DataType.currentItem().text()
        file = self.outputpath+re.sub(' ','_',str(current_regatta))+".cla"
        
        fileType = QtCore.QString("cla *.cla")
        fileName = QtGui.QFileDialog.getSaveFileName(None,"Save As...",
                                                            "./saved_data",
                                                            "cla *.cla",
                                                            fileType
                                                            )
        ext = str(fileType).split(" ")
        if ext[0] == "cla":
            FileExt = ".cla"
            if fileName[-4:] == FileExt:
                FileExt = ""
            fname = fileName+FileExt
                                                            
        
        FO = open(fname, "w")
        for y in range (0, DataSource.rowCount()):
            skipper = str(DataSource.item(y,0).text())
            races = []
            for x in range(1, DataSource.columnCount()-1):
                races.append(str(DataSource.item(y,x).text()))
            riga = "%s="%(skipper)+",".join(races)
            FO.write(riga)
            FO.write("\n")
        FO.close()
            
    def CheckRegatta(self):
        if self.L_Regattas.currentItem() == None:
            self.ShowWarningDialog("Please select a regatta.\n")
            return

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
        pass
   
    def UpdateRegattaRanking(self):
        self.SaveRankingData()
        self.LoadRegattaRanking()


    def CancelRegatta(self):
        item = self.L_Regattas.selectedItems()
        self.L_Regattas.setCurrentItem(item[0])
        pos = self.L_Regattas.currentRow()
        current_reg = self.L_Regattas.item(pos).text()
        file = self.inputpath+re.sub(' ','_',str(current_reg))+".cla"
        os.remove(file)
        self.LoadData()
    
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
    
            
    def SaveClassRank(self):
        self.SaveRankingData(self.L_Classi, self.T_GeneralRanking)
    
        
    def SaveRegattaRank(self):
        self.SaveRankingData(self.L_Regattas, self.T_DetailRanking)

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
QtCore.QObject.connect(ui.T_DetailRanking, QtCore.SIGNAL("itemSelectionChanged ()"), ui.CheckRegatta)
QtCore.QObject.connect(ui.B_Legenda, QtCore.SIGNAL("clicked()"), ui.ShowLegenda)
QtCore.QObject.connect(ui.B_CalcRanking, QtCore.SIGNAL("clicked()"), ui.UpdateRegattaRanking)
QtCore.QObject.connect(ui.B_CancelRegatta, QtCore.SIGNAL("clicked()"), ui.CancelRegatta)
QtCore.QObject.connect(ui.B_DeleteSkipper, QtCore.SIGNAL("clicked()"), ui.CancelSkipper)
QtCore.QObject.connect(ui.B_DeleteRace, QtCore.SIGNAL("clicked()"), ui.CancelRace)

QtCore.QObject.connect(ui.B_SaveClassRank, QtCore.SIGNAL("clicked()"), ui.SaveClassRank)
QtCore.QObject.connect(ui.B_SaveRegattaRank, QtCore.SIGNAL("clicked()"), ui.SaveRegattaRank)
QtCore.QObject.connect(ui.B_ExportClassRank, QtCore.SIGNAL("clicked()"), ui.ExportClassRank)
QtCore.QObject.connect(ui.B_ExportRegattaRank, QtCore.SIGNAL("clicked()"), ui.ExportRegattaRank)


ui.LoadData()

window.show()
sys.exit(app.exec_())


