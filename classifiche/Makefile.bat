echo on

call c:\Python24\pyuic4 gui\main_win.ui -o modules\MainWin.py
call c:\Python24\pyuic4 gui\MainWindow.ui -o modules\MainWindow.py
call c:\Python24\pyuic4 gui\class_dialog.ui -o modules\ClassDialog.py
call c:\Python24\pyuic4 gui\regatta_dialog.ui -o modules\RegattaDialog.py
call c:\Python24\pyuic4 gui\legenda_dialog.ui -o modules\LegendaDialog.py
