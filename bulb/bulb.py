import sys,copy, random, re, os, ConfigParser

from PyQt4 import QtGui, QtCore, uic, Qt

from MainWin import Ui_D_Naca

class RenderArea(QtGui.QWidget):
    points = QtGui.QPolygon([
        QtCore.QPoint(0, 15),
        QtCore.QPoint(10, 30),
        QtCore.QPoint(20, 45),
        QtCore.QPoint(30, 40)
    ])

    Polyline = range(13)
    
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.shape = RenderArea.Polyline
        self.pen = QtGui.QPen()
        self.brush = QtGui.QBrush()
        self.antialiased = False
        self.transformed = False
        self.pixmap = QtGui.QPixmap()
        self.pixmap.load(":/images/qt-logo.png")

        self.setBackgroundRole(QtGui.QPalette.Base)

    def minimumSizeHint(self):
        return QtCore.QSize(100, 100)

    def sizeHint(self):
        return QtCore.QSize(400, 200)

    def setShape(self, shape):
        self.shape = shape
        self.update()

    def setPen(self, pen):
        self.pen = pen
        self.update()

    def setBrush(self, brush):
        self.brush = brush
        self.update()

    def setAntialiased(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def setTransformed(self, transformed):
        self.transformed = transformed
        self.update()

    def paintEvent(self, event):
        
        path = QtGui.QPainterPath()
        path.moveTo(0, 0)
        # per come ho capito, bisogna fare una cosa del tipo:
        # cubicTo ([inizio], [primo punto],[secondopunto]) per la prima
        # poi cubicTo([punto_n-1],[punto_n],[punto_n+1]) per gli altri.
        #considerando la scala e l'offset
        path.cubicTo(0, 0,40,50, 120,70)
        
        path.cubicTo(120, 70,150, 80,400,0)
        
        #startAngle = 30 * 16
        #arcLength = 120 * 16

        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        if self.antialiased:
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.save()
        painter.translate(0, 0)
        painter.drawLine(0,0,400,0)
        painter.drawPath(path)

        painter.restore()

        painter.end()


class MainWin(Ui_D_Naca):
    
    matchRaceList = []
    skipperList = []
    outputpath = ''
    i18npath = ''

    def __init__(self):
        self.ra = RenderArea()
        
        
    def DrawTest(self):
        print "ciao"
    
app = QtGui.QApplication(sys.argv)
window = QtGui.QDialog()
ui = MainWin()
translator = QtCore.QTranslator()
translator.load(QtCore.QString(ui.i18npath+'i18n_it'))
QtGui.qApp.installTranslator(translator)

ui.setupUi(window)
ui.vboxlayout1.addWidget(ui.ra)

QtCore.QObject.connect(ui.B_Print, QtCore.SIGNAL("clicked()"), ui.DrawTest)

window.show()
sys.exit(app.exec_()) 