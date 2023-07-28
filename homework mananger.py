import sys
import typing
from PyQt6.QtWidgets import *
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QDialog
from PyQt6.QtGui import QIcon, QTextCharFormat, QBrush, QColor, QPen, QRegion
from PyQt6.QtCore import Qt, QRect, QPoint
from PyQt6 import uic
from PyQt6.uic import loadUi
import sqlite3
import datetime
from PyQt6.QtGui import QFont

from PyQt6.QtCore import Qt, QRectF, QDate, QSize
from PyQt6.QtGui import QPainter, QColor, QFont, QBrush



cruk_size = int(4)
cruk_w = int(4)
cruk_h = int(4)


(Ui_MainWindow, QMainWindow) = uic.loadUiType('homework.ui')

class MainWindow(QMainWindow, Ui_MainWindow, QWidget):

    """MainWindow inherits QMainWindow"""

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setGeometry(450, 200, 500, 550)   # создание окна
        self.setWindowTitle("Menanger")
        self.WIcon = QIcon('WIcon.png')
        self.setWindowIcon(self.WIcon)
        loadUi('homework.ui', self)
        self.create_Homework_btn.clicked.connect(lambda: self.create_homework_2())

        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(-1, 9, 9, 9)
        self.date2 = ""
        self.gh_text = ""
        self.create_table()
        self.table_mashtab()
        
        # индекс для проверки сдачи сорт
        self.prov_index = True
        self.current_new_object = False
        
        # сигналы
        self.btn_create_calen.clicked.connect(self.go_screen_3)
        self.btn_sdaci_calen.clicked.connect(self.go_screen_2)
        self.twg.cellClicked.connect(self.cellClicked)
        self.btn_nedavnii.clicked.connect(self.nedavne_vapol_window)
        self.str_o.activated.connect(self.start_sortirovka)

        # конектимся с базой данных и синхронизируем какой вид сортировки был при закрытие приложенияs
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """SELECT sort_index FROM sort_index WHERE rowid = 1"""
        sort_index = cursor.execute(query).fetchall()
        self.prosh_str_o = sort_index[0][0]
        self.str_o.setCurrentIndex(sort_index[0][0])


        # disayn
        self.create_Homework_btn.setStyleSheet("QPushButton{color: black; background-color: rgb(255, 170, 33);; border-radius: 8px; border: 2px; font:  22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        
        self.btn_create_calen.setStyleSheet("QPushButton{color: black; background-color: rgb(255, 170, 33);; border-radius: 8px; border: 2px; font:  22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        
        self.btn_sdaci_calen.setStyleSheet("QPushButton{color: black; background-color: rgb(255, 170, 33);; border-radius: 8px; border: 2px; font:  22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        
        self.btn_nedavnii.setStyleSheet("QPushButton{color: #eefa05; background-color: #e64027; border-radius: 12px; border: 2px; font: 22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        
        self.str_o.setStyleSheet((""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 12;
    color: black;
    font: 16pt 'MS Shell Dlg 2';                        
                                  
}

QComboBox:editable {
    background: white;                      
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
  
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1); 
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;                            
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 3px solid darkgray;
    selection-background-color: lightgray;
    border-radius: 8px;
}

"""))


    def start_sortirovka(self):

        print("Происходит выбор сортировки")
        db = sqlite3.connect('htbase.db')
        curosr = db.cursor()
        func_1 = (self.str_o.currentIndex(), 1)
        query = """UPDATE sort_index SET sort_index=? WHERE rowid = ?"""      
        curosr.execute(query, func_1)
        db.commit()
       
            
        # определяем как сортировать
        if self.str_o.currentIndex() == 0:
            if self.prosh_str_o != 0:
                #print("сортировка по ближайщей дате сдачи")
                self.prosh_str_o = 0
                return self.sdachi_sortirovka()
        elif self.str_o.currentIndex() == 2:
            if self.prosh_str_o != 2:
                #print("Сортировка по дате созданию(по увеличеню)")
                self.prosh_str_o = 2
                return self.create_sortirovka()             
        elif self.str_o.currentIndex() == 1:
            if self.prosh_str_o != 1:
                #print("обратная сортировка по дате сдачи")
                self.prosh_str_o = 1
                return self.obr_sdachi_sort()
        elif self.str_o.currentIndex() ==3:
            if self.prosh_str_o != 3:
                #print("Сортировка по количеству Дз")
                self.prosh_str_o = 3 
                return self.kolichestven_sort()
       

    def kolichestven_sort(self):
        # индекс для проверки сдачи сорт
        self.prov_index = True
        # конеткимся с базой данных и получаем все значения для дальнейшей обработки
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """SELECT * FROM hometask"""
        result = cursor.execute(query).fetchall()
        db.close()

        # подготовка к  сортировке
        n = len(list(result))
        result_2 = result
        obres = [] # предметы тож для сортировки
        polusort = [] # знаки для дальнейшей сортирвки
        fullsort = []
        for i in range(n):
            obres.append(result_2[i][3])
        for i in range(n):
            polusort.append(obres.count(result_2[i][3]))
        ne_obres = obres.copy()
        nulp = ["Алгебра", "Геометрия", "Русский Язык", "Англисский язык", "Химия", "Информатика", "Физика", "Физкультура", "История", "Обществознание", "Литература", "География", "Обж"]
        replace_nulp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        for i in range(n):
            for t in range(len(nulp)):
                if obres[i] == nulp[t]:
                    obres[i] = replace_nulp[t]
        
        d = list(zip(polusort, ne_obres))
        
        # сама сортровка

        for i in range(n-1):
            for t in range(n - i - 1):
                if d[t][0] > d[t+1][0]:
                    d[t], d[t+1] = d[t+1], d[t]
                    result_2[t], result_2[t+1] = result_2[t+1], result_2[t]
                elif d[t][0] == d[t+1][0]:
                    if d[t][1] > d[t+1][1]:
                        d[t], d[t+1] = d[t+1], d[t]
                        result_2[t], result_2[t+1] = result_2[t+1], result_2[t]
        
        result_2 =result_2[::-1]
        # изменяем таблицу в базе данных
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        for i in range(n):
            nel = (str(result_2[i][0]), str(result_2[i][2]), str(result_2[i][3]), str(result_2[i][1]), i+1,)
            query = """ UPDATE hometask SET data_create= ?, data_sdachi= ?, predmet =?, homework_text= ? WHERE rowid = ?  """
            cursor.execute(query, nel)
            db.commit()
            self.twg.removeRow(0)
           
            
        # перерисовываем таблицу в приложении
        self.check_pere = True
        self.create_table()


    def sdachi_sortirovka(self):
        # конеткимся с базой данных и получаем все значения для дальнейшей обработки
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """SELECT * FROM hometask"""
        result = cursor.execute(query).fetchall()
        db.close()
        result_2 = result

        # сама сортировка
        def quicksort(alist, start, end):
            '''Sorts the list from indexes start to end - 1 inclusive.'''
            if end - start > 1:
                p = partition(alist, start, end)
                quicksort(alist, start, p)
                quicksort(alist, p + 1, end)
        
        
        def partition(alist, start, end):
            pivot = alist[start]
            i = start + 1
            j = end - 1
        
            while True:
                while (i <= j and alist[i] <= pivot):
                    i = i + 1
                while (i <= j and alist[j] >= pivot):
                    j = j - 1
        
                if i <= j:
                    alist[i], alist[j] = alist[j], alist[i]
                    result_2[i], result_2[j] = result_2[j], result_2[i]

                else:
                    alist[start], alist[j] = alist[j], alist[start]
                    result_2[start], result_2[j] = result_2[j], result_2[start]
                    return j
                    # конец сортировки
        # подготовка к сортировке
        n = len(list(result_2))
        alist = []
        for i in range(n):
            alist.append(result_2[i][2])
        quicksort(alist, 0, len(alist))
        
        
       
        # изменяем таблицу в базе данных
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        for i in range(n):
            nel = (str(result_2[i][0]), str(result_2[i][2]), str(result_2[i][3]), str(result_2[i][1]), i+1,)
            query = """ UPDATE hometask SET data_create= ?, data_sdachi= ?, predmet =?, homework_text= ? WHERE rowid = ?  """
            cursor.execute(query, nel)
            db.commit()
            self.twg.removeRow(0)
           
        # перерисовываем таблицу в приложении
        self.check_pere = True
        self.create_table()
        self.prov_index = True


    def obr_sdachi_sort(self):
        # индекс для проверки сдачи сорт
        self.prov_index = True
        # конеткимся с базой данных и получаем все значения для дальнейшей обработки
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """SELECT * FROM hometask"""
        result = cursor.execute(query).fetchall()
        db.close()
        result_2 = result

        # сама сортировка
        def quicksort(alist, start, end):
            '''Sorts the list from indexes start to end - 1 inclusive.'''
            if end - start > 1:
                p = partition(alist, start, end)
                quicksort(alist, start, p)
                quicksort(alist, p + 1, end)
        
        
        def partition(alist, start, end):
            pivot = alist[start]
            i = start + 1
            j = end - 1
        
            while True:
                while (i <= j and alist[i] <= pivot):
                    i = i + 1
                while (i <= j and alist[j] >= pivot):
                    j = j - 1
        
                if i <= j:
                    alist[i], alist[j] = alist[j], alist[i]
                    result_2[i], result_2[j] = result_2[j], result_2[i]
                else:
                    alist[start], alist[j] = alist[j], alist[start]
                    result_2[start], result_2[j] = result_2[j], result_2[start]
                    return j
                    # конец сортировки
        # подготовка к сортировке
        n = len(list(result_2))
        alist = []
        for i in range(n):
            alist.append(result_2[i][2])
        quicksort(alist, 0, len(alist))

        result_2 = result_2[::-1]
        # изменяем таблицу в базе данных
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        for i in range(n):
            nel = (str(result_2[i][0]), str(result_2[i][2]), str(result_2[i][3]), str(result_2[i][1]), i+1,)
            query = """ UPDATE hometask SET data_create= ?, data_sdachi= ?, predmet =?, homework_text= ? WHERE rowid = ?  """
            cursor.execute(query, nel)
            db.commit()
            self.twg.removeRow(0)
           
            
        # перерисовываем таблицу в приложении
        self.check_pere = True
        self.create_table()


    def create_sortirovka(self):
        # индекс для проверки сдачи сорт
        self.prov_index = True
        # конеткимся с базой данных и получаем все значения для дальнейшей обработки
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """SELECT * FROM hometask"""
        result = cursor.execute(query).fetchall()
        db.close()

        result_2 = result
        # сама сортировка
        def quicksort(alist, start, end):
            '''Sorts the list from indexes start to end - 1 inclusive.'''
            if end - start > 1:
                p = partition(alist, start, end)
                quicksort(alist, start, p)
                quicksort(alist, p + 1, end)
        
        
        def partition(alist, start, end):
            pivot = alist[start]
            i = start + 1
            j = end - 1
        
            while True:
                while (i <= j and alist[i] <= pivot):
                    i = i + 1
                while (i <= j and alist[j] >= pivot):
                    j = j - 1
        
                if i <= j:
                    alist[i], alist[j] = alist[j], alist[i]
                    result_2[i], result_2[j] = result_2[j], result_2[i]
                else:
                    alist[start], alist[j] = alist[j], alist[start]
                    result_2[start], result_2[j] = result_2[j], result_2[start]
                    return j
                    # конец сортировки
        # подготовка к сортировке
        n = len(list(result_2))
        alist = []
        for i in range(n):
            alist.append(result_2[i][0])
        quicksort(alist, 0, len(alist))
      
        # изменяем таблицу в базе данных
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        for i in range(n):
            nel = (str(result_2[i][0]), str(result_2[i][2]), str(result_2[i][3]), str(result_2[i][1]), i+1,)
            query = """ UPDATE hometask SET data_create= ?, data_sdachi= ?, predmet =?, homework_text= ? WHERE rowid = ?  """
            cursor.execute(query, nel)
            db.commit()
            self.twg.removeRow(0)
           
            
        # перерисовываем таблицу в приложении
        self.check_pere = True
        self.create_table()


    def nedavne_vapol_window(self):
        window.close()
        nedavnee_vapol_window.show()
        nedavnee_vapol_window.create_table()


    def go_screen_3(self):
        window.close()
        create_calen_window.show()
    

    def check_box(self):
        # алгоритм удаления 
        crow = self.twg.currentRow()
        bb = (int(crow+1),)
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()

        m = """DELETE FROM hometask WHERE rowid = ? """
        j = """SELECT rowid FROM hometask"""
        dek = """SELECT * FROM hometask WHERE rowid =?"""
        up = """INSERT INTO nedavno_ydal(data_create, predmet, data_sdachi, homework_text, vabor) VALUES(?,?,?,?,?)"""
        vac = """VACUUM"""
        cursor.execute(vac)

        n = cursor.execute(dek, bb).fetchall()
        up_box = n[0][0], n[0][3], n[0][2], n[0][1], "False"
        cursor.execute(up, up_box)
        cursor.execute(m, bb)


        db.commit()
        self.twg.removeRow(crow)


    def go_screen_2(self):
        self.close()
        sdacha_calen_window.show()


    def table_mashtab(self):
        self.wh = self.height()
        self.ww = self.width()


        # делаем расчет масштабируем табл
        self.x_1 = int(self.ww / 100 * 30)
        self.x_3 = int(self.ww / 100 * 20)
        self.x_0 = int(self.ww / 100*2)
        self.x_2 = int(self.ww / 100*20)

        # масштабтрование табл
        self.twg.setColumnWidth(0, 80)
        self.twg.setColumnWidth(1, 150)
        self.twg.setColumnWidth(2, 140)


    def create_table(self):

        # это нужно для цикла for
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        jay = """SELECT COUNT(data_create) FROM hometask"""

        cursor.execute(jay)

        db.commit()
        self.pasa = (cursor.fetchall()[0][0])
        
        

        for i in range(self.pasa):
            if i+1 > self.twg.rowCount() or self.check_pere == True or self.current_new_object == True:

                db = sqlite3.connect("htbase.db")
                cursor = db.cursor()
                query = """SELECT * from hometask"""
                cursor.execute(query)
                arr = cursor.fetchall()  # доступ к базе данных по индексу
                

                db.commit()

                self.twg.setShowGrid(True)
                self.rowPosition = self.twg.rowCount()
                self.twg.insertRow(self.rowPosition)

                # для табл шаблоны
                self.gh_table_1 = QCheckBox()
                i_3 = QLabel(arr[i][3])
                i_2 = QLabel(arr[i][1])
                i_1 =  QLabel(arr[i][2])
                i_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
                i_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
                i_1.setAlignment(Qt.AlignmentFlag.AlignCenter)
                

                # заполняем табл
                self.twg.setCellWidget(self.rowPosition, 1,  i_3)
                self.twg.setCellWidget(self.rowPosition, 2, i_1)
                self.twg.setCellWidget(self.rowPosition, 3, i_2)
                self.twg.setCellWidget(self.rowPosition, 0, self.gh_table_1)
                self.gh_table_1.clicked.connect(self.check_box)
                self.gh_table_1.setChecked(False)
        self.check_pere = False
        self.current_new_object = False


    def cellClicked(self, row, column):
        cell_click.gain_resurs(row, self)
        cell_click.show()


    # расчет процентов для табл
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        self.table_mashtab()


    def __del__(self):
        self.ui = None


    def create_homework_2(self):
        create_Homework.show()
        create_Homework.gain_fain(self)


class sdacha_calen_window(QMainWindow, QWidget, Ui_MainWindow):
    def __init__(self):
        super(sdacha_calen_window, self).__init__()
        loadUi('create_calen.ui', self)
        self.calendar = MyCalendar_S()
        self.create_lbl = self.sdacha_lbl
        self.setWindowTitle("Календарь сдачи")
        self.setWindowIcon(QIcon('kalendar.png'))
        # добавляем кастомный календарь
        self.vl_kal.removeWidget(self.calendarWidget)
        self.vl_kal.removeWidget(self.gotovo_btn)
        self.vl_kal.addWidget(self.calendar)
        self.vl_kal.addWidget(self.gotovo_btn)
        self.calendarWidget.close()

        # мелочи с интерфейсом
        self.gotovo_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); border-radius: 7px;  font: 18pt ; border: 3px; background-color: rgb(255,151,0);}"
                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: rgb(255, 255, 0);}"
                                      "QPushButton:pressed{background: rgb(0,0,0); color: red}")
        self.sost_lbl.setText("День сдачи не указан")
        self.label.setText("Выберите день сдачи")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.predmert_box.setStyleSheet(""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 6;
    color: black
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

""")


        # сигналы
        self.gotovo_btn.clicked.connect(self.gotovo)
        self.calendar.clicked.connect(self.get_text_homework)



    def gotovo(self):
        sdacha_calen_window.close()
        window.show()


    def get_text_homework(self):
        self.hwte.setText("")
        self.predmert_box.clear()
        self.sdacha_lbl.setText("")
        #self.predmert_box.setText("выберите предмет")
        # сравнимаем два календаря на даты
        self.data_now = self.calendar.selectedDate()
        self.data_now = self.data_now.toPyDate()
        
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        row = (self.data_now,)
        quary = """SELECT predmet, homework_text, data_create FROM hometask WHERE data_sdachi = ?"""  # дынные о предмете, о дз, о дате сдачи 
        quary_2 = """SELECT COUNT(predmet) FROM hometask WHERE data_sdachi = ?""" # количество предметов на этот день
        y = cursor.execute(quary_2, row).fetchall()[0][0]  # выполняем что в предедкщие строке
        self.h = cursor.execute(quary, row).fetchall()
        # получили данные заполняем Qcombobox на предметы
        if y != 0:
            j = "Найдено " + str(y) + " ДЗ"
            self.sost_lbl.setText(j)
            for i in range(y):
                self.predmert_box.addItem(self.h[i][0])
        else:
            self.sost_lbl.setText("ДЗ не найдено")
        self.predmert_box.activated.connect(lambda: self.prov_in_predmet())

    # заполняем данные когда пользователь выьирает другой предмет в данном дне
    def prov_in_predmet(self):
        self.sdacha_lbl.setText("")
        self.hwte.setText(self.h[self.predmert_box.currentIndex()][1])
        if self.h[self.predmert_box.currentIndex()][2] != "":
            ne_h = str("Созданно:  ") + str(self.h[self.predmert_box.currentIndex()][2])
            self.sdacha_lbl.setText(ne_h)
        else:
            self.sdacha_lbl.setText("Срок здачи не указан")


    def resizeEvent(self, a0) -> None:
        global cruk_h, cruk_w, cruk_size
        # мастабирование и дизайн окна
        wsw = sdacha_calen_window.width()
        wsh = sdacha_calen_window.height()
        cal_wsw = int(wsw/100 *60)
        lbl_wsw = int(wsw - cal_wsw)
        otstup  = int(wsw/100 * 2)
        
        self.cal_w.resize(int(cal_wsw - otstup), int(wsh - otstup))
        self.lbl_w.resize(lbl_wsw - otstup, wsh - otstup)
        self.lbl_w.move(cal_wsw, 0)




        ws = wsw + wsh
     
        # расчитывем размер текста для всех объектов
        self.hw_font_func = QFont()
        self.sost_lbl_fonc_func = QFont()
        if ws > 1150:
            poi = int((ws-1150)//320)
            self.hw_font_func.setPointSize(14+poi)
            self.sost_lbl_fonc_func.setPointSize(14+poi)
        elif ws< 1150:
            poi_2 = int((ws-1150)//105)
            self.hw_font_func.setPointSize(14+poi_2)
            self.sost_lbl_fonc_func.setPointSize(14+poi_2)
        else:
            self.hw_font_func.setPointSize(14)
            self.sost_lbl_fonc_func.setPointSize(14)

        self.predmert_box_font_func = QFont()
        self.predmert_box_font_func.setPointSize(int(ws//64))
        
        self.gotovo_font_func = QFont()
        self.gotovo_font_func.setPointSize(int(ws//52.2))
        

        self.label_font_func = QFont()
        self.label_font_func.setPointSize(int(ws//44.2))
        
        
        
        self.cw_font_func = QFont()
        self.cw_font_func.setPointSize(int(ws//115))

        cruk_size = ws//304
        cruk_w = wsw//50
        cruk_h = wsh//35

        # задаем разер текста для всех обЪектов
        self.hwte.setFont(self.hw_font_func)
        self.predmert_box.setFont(self.predmert_box_font_func)
        self.sdacha_lbl.setFont(self.predmert_box_font_func)
        self.label.setFont(self.label_font_func)
        self.gotovo_btn.setFont(self.gotovo_font_func)
        self.sost_lbl.setFont(self.sost_lbl_fonc_func)
        self.calendar.setFont(self.cw_font_func)


    def closeEvent(self, event):
        self.hwte.setText("")
        self.predmert_box.clear()
        self.sdacha_lbl.setText("")
    
    
class create_Homework(QDialog):
    def __init__(self):
        super(create_Homework, self).__init__()
        self.date2 = ""
        self.create_Homework_1()
        W_icon = QIcon('create_homework_icon')
        self.setWindowIcon(W_icon)
        self.setWindowTitle("Запишите Домашнее задание")


    def create_Homework_1(self):
        self.setMinimumSize(400, 475)
        self.resize(400, 475)
        self.setWindowTitle("Menanger")

        self.gain_homework_lbl = QLabel("Записать ДЗ", self)
        self.gain_homework_lbl.setGeometry(2, 149, 396, 35)
        self.gain_homework_lbl.setStyleSheet("background-color: #f09a05;")
        self.gain_homework_lbl.setFont(QtGui.QFont("Times", 24))
        self.gain_homework_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
        self.gain_homework_choise_predmet = QComboBox(self)
        self.gain_homework_choise_predmet.setGeometry(2, 3, 150, 33)
        self.gain_homework_choise_predmet.addItems(["Алгебра", "Геометрия", "Русский Язык", "Англисский язык", "Химия", "Информатика", "Физика", "Физкультура", "История", "Обществознание", "Литература", "География", "Обж"])
        self.gain_homework_choise_predmet.setStyleSheet(""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 6;
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

""")

        self.gain_homework_get_hoomework = QTextEdit(self)
        self.gain_homework_get_hoomework.setGeometry(2, 184, 396, 250)

        self.gain_homework_calendar_btn = QPushButton("Выбрать дату сдачи ДЗ", self)
        self.gain_homework_calendar_btn.setGeometry(250, 3, 150, 25)
        self.gain_homework_calendar_btn.clicked.connect(self.calen_show)
        self.gain_homework_calendar_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: #14d4de; border-radius: 6px; border: 2px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color: black}""")


        self.gain_homework_finish_btn = QPushButton("Сохранить", self)
        self.gain_homework_finish_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: #14d4de; border-radius: 6px; border: 2px;}"
                                                    "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                    "QPushButton:pressed{background: solid grey; color: red}""")
        self.gain_homework_finish_btn.setGeometry(75, 437, 250, 35)
        self.gain_homework_finish_btn.clicked.connect(self.process_homework_finished)


    def calen_show(self):
        self.calen = QtWidgets.QDialog(self)
        self.calen.setWindowTitle("Календарь")
        self.calen.setWindowIcon(QIcon('kalendar.png'))
        self.calen.resize(400, 380)

        self.gain_homework_data_vapol = BaseCustomCalendar(self.calen)

        hbox = QVBoxLayout()
        hbox.addWidget(self.gain_homework_data_vapol)
        hbox.setContentsMargins(6, 6, 6, 6)
        self.calen.setLayout(hbox)

        calen_save = QPushButton("Сохранить", self.calen)
        calen_save.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: green; border-radius: 12px; border: 2px;font: 50 22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")

        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setVerticalStretch(8)
        calen_save.setSizePolicy(sizePolicy1)
        hbox.addWidget(calen_save)
        calen_save.clicked.connect(self.safe_calen)

        result = self.calen.exec()


    def process_homework_finished(self):
        self.close()
        self.gh_text = self.gain_homework_get_hoomework.toPlainText()

        self.gh_predmet = self.gain_homework_choise_predmet.currentText()

        self.gh_date_now = datetime.date.today()

        with sqlite3.connect('htbase.db') as db:
            cursor = db.cursor()
            query = """ INSERT INTO hometask(data_create, data_sdachi, predmet, homework_text) VALUES(?,?,?,?)  """
            row = (self.gh_date_now, self.date2, self.gh_predmet, self.gh_text)

            cursor.execute(query, row)
            db.commit()

        self.prosh_str_o = "w"
        self.ui.prosh_str_o = "w"
        self.ui.start_sortirovka()



    def resizeEvent(self, a0):
        h = self.height()
        w = self.width()
        self.gain_homework_lbl.resize(self.width()-4, int(h*0.075))
        self.gain_homework_choise_predmet.resize(int(w*0.375), int(h*0.07))
        self.gain_homework_calendar_btn.resize(int(w*0.375), int(h*0.07))
        self.gain_homework_finish_btn.resize(int(w*0.625), int(h*0.075))
        self.gain_homework_get_hoomework.resize(w-4, int(h*0.526))

        self.gain_homework_calendar_btn.move(w-3-int(w*0.375), 3)
        self.gain_homework_finish_btn.move(int((w-int(w*0.625))/2), h-int(h*0.080)-int(h*0.006))
        self.gain_homework_get_hoomework.move(2, int(h*0.38))
        self.gain_homework_lbl.move(2, int(h*0.31))
    

    def safe_calen(self):
        self.date_calen = self.gain_homework_data_vapol.selectedDate()
        self.date2 = self.date_calen.toPyDate()
        self.calen.close()


    def gain_fain(self, ui):
        self.ui = ui


class cell_click(QDialog, QWidget):


    def __init__(self):
        super(cell_click, self).__init__()
        self.sdachi_calen = BaseCustomCalendar_y()
        self.resize(676, 449)
        self.setMinimumSize(571, 395)
        self.setWindowTitle("Просмотр дз")
        self.setWindowIcon(QIcon('glaz_3.jpg'))
        self.settings_sost = "close"
        self.sost_radia_func = False
        
        self.lbl_w = QWidget(self)
        self.lbl_w.setObjectName(u"lbl_w")
        self.lbl_w.setGeometry(QRect(350, 10, 301, 441))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(40)
        self.lbl_w.setSizePolicy(sizePolicy)
        self.verticalLayout_7 = QVBoxLayout(self.lbl_w)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 2, 0)
        self.predmet_box = QComboBox(self.lbl_w)
        self.predmet_box.setObjectName(u"predmet_box")
        sizePolicy.setHeightForWidth(self.predmet_box.sizePolicy().hasHeightForWidth())
        self.predmet_box.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"MS Shell Dlg 2")
        font.setPointSize(18)

        font.setWeight(50)
        self.predmet_box.setFont(font)
        self.predmet_box.setStyleSheet(""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 6;
    color: black
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

""")

        self.verticalLayout_7.addWidget(self.predmet_box)

        self.homework_text = QTextEdit(self.lbl_w)
        self.homework_text.setObjectName(u"homework_text")
        self.homework_text.setStyleSheet(u"\n"
"color: rgb(255, 170, 0);")
        self.homework_text.setFrameShape(QFrame.Shape.StyledPanel)

        self.verticalLayout_7.addWidget(self.homework_text)

        self.create_calen_lbl = QLabel("Созданно ",self.lbl_w)
        self.create_calen_lbl.setObjectName(u"create_calen_lbl")
        sizePolicy.setHeightForWidth(self.create_calen_lbl.sizePolicy().hasHeightForWidth())
        self.create_calen_lbl.setSizePolicy(sizePolicy)
        self.create_calen_lbl.setFont(font)

        self.verticalLayout_7.addWidget(self.create_calen_lbl)

        self.cal_w = QWidget(self)
        self.cal_w.setObjectName(u"cal_w")
        self.cal_w.setGeometry(QRect(10, 20, 301, 441))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(60)
        self.cal_w.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.cal_w)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.vl_kal_4 = QVBoxLayout()
        self.vl_kal_4.setSpacing(2)
        self.vl_kal_4.setObjectName(u"vl_kal_4")
        self.vl_kal_4.setContentsMargins(-1, -1, -1, 0)
        self.sdachi_calen_lbl = QLabel("Срок сдачи", self.cal_w)
        self.sdachi_calen_lbl.setObjectName(u"sdachi_calen_lbl")
        font1 = QFont()
        font1.setPointSize(26)
        self.sdachi_calen_lbl.setFont(font1)
        self.sdachi_calen_lbl.setStyleSheet(u"\n"
"color: rgb(170, 85, 255);")
        
        self.vl_kal_4.addWidget(self.sdachi_calen_lbl)
        self.vl_kal_4.addWidget(self.sdachi_calen)

        self.Finish_btn = QPushButton("Gotovo", self.cal_w)
        self.Finish_btn.setObjectName(u"Finish_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(7)
        self.Finish_btn.setSizePolicy(sizePolicy3)
        font3 = QFont()
        font3.setFamily(u"Niagara Engraved")
        font3.setPointSize(1)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.Finish_btn.setFont(font3)
        self.Finish_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255,151,0);\n"
"border-radius: 12px; \n"
"border: 3px;\n"
"\n"
"")
        self.vl_kal_4.addWidget(self.Finish_btn)
        self.verticalLayout_8.addLayout(self.vl_kal_4)
        self.other()

        
    def gain_resurs(self, row, ui):
        self.row = row
        self.ui = ui
        hl = (self.row + 1,)
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        vac = """VACUUM"""
        cursor.execute(vac)
        quary = """SELECT * from hometask WHERE rowid = ?"""
        res = cursor.execute(quary, hl).fetchall()
        self.troling = res
        db.commit()
        if res[0][2] != "":
            b = datetime.datetime.strptime(res[0][2], '%Y-%m-%d').date()
            date = QtCore.QDate(b)
            self.sdachi_calen.setSelectedDate(date)
                

        create_text = "Созданно " + res[0][0]
        self.homework_text.setText(res[0][1])
        self.predmet_box.setCurrentText(res[0][3])
        self.create_calen_lbl.setText(create_text)

    
    def resizeEvent(self, a0) -> None:        
        wsw = cell_click.width()
        wsh = cell_click.height()
        cal_wsw = int(wsw/100 *60)
        lbl_wsw = int(wsw - cal_wsw)
        otstup  = int(wsw/100 * 2)

        # layout
        self.cal_w.setGeometry(5, 5, int(wsw/100*0.6)-5, wsh-10)
        self.lbl_w.setGeometry(10 +int(wsw/100*0.6)-5, 5, int(wsw/100*0.4)-10, wsh-10)
        self.settings_btn.setGeometry(10, 10, int((wsw+ wsh)/30), int((wsw+ wsh)/30))
        
        self.cal_w.resize(cal_wsw - otstup, wsh - otstup)
        self.lbl_w.resize(lbl_wsw - otstup, wsh - otstup)
        self.lbl_w.move(cal_wsw, 0)
        

        ws = wsw + wsh
     
        # расчитывем размер текста для всех объектов
        self.hw_font_func = QFont()
        self.sdachi_calent = QFont()
        if ws > 1150:
            poi = int((ws-1150)//320)
            self.hw_font_func.setPointSize(14+poi)
            self.sdachi_calent.setPointSize(14+poi)
        elif ws< 1150:
            poi_2 = int((ws-1150)//105)
            self.hw_font_func.setPointSize(14+poi_2)
            self.sdachi_calent.setPointSize(14+poi_2)
        else:
            self.hw_font_func.setPointSize(14)
            self.sdachi_calent.setPointSize(14)

        self.predmet_box_font_func = QFont()
        self.predmet_box_font_func.setPointSize(int(ws//64))
        
        self.Finish_btn_font_func = QFont()
        self.Finish_btn_font_func.setPointSize(int(ws//52.2))
        

        self.label_font_func = QFont()
        self.label_font_func.setPointSize(int(ws//44.2))
        
        
        
        self.cw_font_func = QFont()
        self.cw_font_func.setPointSize(int(ws//115))


        # задаем разер текста для всех обЪектов
        self.homework_text.setFont(self.sdachi_calent)
        self.predmet_box.setFont(self.predmet_box_font_func)
        self.create_calen_lbl.setFont(self.predmet_box_font_func)
        self.sdachi_calen_lbl.setFont(self.label_font_func)
        self.Finish_btn.setFont(self.Finish_btn_font_func)
        self.sdachi_calen.setFont(self.cw_font_func)
        self.settings_btn.setIconSize(QSize(int((wsw+ wsh)/30), int((wsw+ wsh)/30)))
        self.settings_btn.setStyleSheet("QPushButton{color: #f29411; background-color: green; border-radius: 16px; border: 4px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        

    def other(self):
        if self.sost_radia_func == False:
            self.predmet_box.setEnabled(False)
            self.homework_text.setReadOnly(True)
            self.sdachi_calen_lbl.setText("срок здачи")
            self.sdachi_calen.setSelectionMode(QCalendarWidget.SelectionMode.NoSelection)

        elif self.sost_radia_func == True:
            self.predmet_box.setEnabled(True)
            self.homework_text.setReadOnly(False)
            self.sdachi_calen_lbl.setText("Изменить срок здачи")
            self.sdachi_calen.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)

        self.create_calen_lbl.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.sdachi_calen_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.homework_text.setStyleSheet("color: rgb(255, 170, 0); font: 75 12pt 'Microsoft YaHei UI';")
        self.Finish_btn.setStyleSheet("QPushButton{color: #eefa05; background-color: #e64027; border-radius: 12px; border: 2px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        self.predmet_box.addItems(
            ["Алгебра", "Геометрия", "Русский Язык", "Англисский язык", "Химия", "Информатика", "Физика",
            "Физкультура", "История", "Обществознание", "Литература", "География", "Обж"])
        
        self.settings_btn = QPushButton(self)
        self.settings_btn.setStyleSheet("QPushButton{color: #f29411; background-color: green; border-radius: 16px; border: 4px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        vbn = QIcon('settings_icon.jpg')
        self.settings_btn.setIcon(vbn)
        self.settings_btn.setToolTip("Настройки")
        
        
        self.lbl = QLabel("Разрешить изменения", self)
        self.radio = QCheckBox("", self)
        self.lbl.setVisible(False)
        self.radio.setVisible(False)
        self.proverka_calendar_sdachi_see = False    
        
        self.Finish_btn.clicked.connect(lambda: self.Finish_func())
        self.settings_btn.clicked.connect(self.settings)
        self.sdachi_calen.clicked.connect(lambda: self.data_sdachi_f())
    

    def data_sdachi_f(self):
         self.proverka_calendar_sdachi_see = True


    def settings(self):
        if self.settings_sost == "close":
            self.lbl_w.setVisible(False)
            self.cal_w.setVisible(False)
            self.settings_sost = "open"
            self.setWindowIcon(QIcon('nastroyki.png'))
            self.setWindowTitle("Настройки")
            self.radio.setGeometry(475, 80, 30, 40)
            self.lbl.setGeometry(70, 80, 400, 40)
            self.lbl.setStyleSheet("font: 75 22pt 'MS Shell Dlg 2';")
            self.radio.setChecked(self.sost_radia_func)
            self.lbl.setVisible(True)
            self.radio.setVisible(True)
            
        elif self.settings_sost == "open":
            g = QIcon('glaz_3.jpg')
            self.setWindowIcon(g)
            self.setWindowTitle("Просмотр дз")
            self.sost_radia_func = self.radio.isChecked()
            print(self.sost_radia_func)
            self.lbl_w.setVisible(True)
            self.cal_w.setVisible(True)
            self.settings_sost = "close"
            self.lbl.setVisible(False)
            self.radio.setVisible(False)

            if self.sost_radia_func == False:
                self.predmet_box.setEnabled(False)
                self.homework_text.setReadOnly(True)
                self.sdachi_calen.setSelectionMode(QCalendarWidget.SelectionMode.NoSelection)
                self.homework_text.setFrameShape(QFrame.Shape.StyledPanel)
                self.sdachi_calen_lbl.setText("Срок здачи")
                self.predmet_box.setStyleSheet(""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 6;
    color: black
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

""")
            
            elif self.sost_radia_func == True:
                self.predmet_box.setEnabled(True)
                self.homework_text.setReadOnly(False)
                self.sdachi_calen.setSelectionMode(QCalendarWidget.SelectionMode.SingleSelection)
                self.sdachi_calen_lbl.setText("Изменить срок здачи")


    def Finish_func(self):
        cell_click.close()
        if self.proverka_calendar_sdachi_see == True:
            self.cycles = self.sdachi_calen.selectedDate().toPyDate()

            sdach = QLabel(str(self.sdachi_calen.selectedDate().toPyDate()))
            sdach.setAlignment(Qt.AlignmentFlag.AlignCenter)

            self.ui.twg.setCellWidget(self.ui.twg.currentRow(), 2, sdach)
        elif self.proverka_calendar_sdachi_see == False and len(self.troling[0][2]) != 4:
            self.cycles = self.troling[0][2]
            print(self.troling)
        else:
            self.cycles = ""
        

        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        query = """ UPDATE hometask SET data_sdachi= ?, predmet =?, homework_text= ? WHERE rowid = ?  """
        row = self.cycles, self.predmet_box.currentText(), self.homework_text.toPlainText(), self.ui.twg.currentRow() + 1
        cursor.execute(query, row)

        db.commit()
        pred = QLabel(str(self.predmet_box.currentText()))
        pred.setAlignment(Qt.AlignmentFlag.AlignCenter)

        home = QLabel(str(self.homework_text.toPlainText()))
        home.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.ui.twg.setCellWidget(self.ui.twg.currentRow(), 1, pred)
        self.ui.twg.setCellWidget(self.ui.twg.currentRow(), 3, home)


    def closeEvent(self, a0) -> None:
        self.lbl_w.setVisible(True)
        self.cal_w.setVisible(True)
        self.lbl.setVisible(False)
        self.radio.setVisible(False)
        return super().closeEvent(a0)


class BaseCustomCalendar(QCalendarWidget):

    def __init__(self, parent=None):
        QCalendarWidget.__init__(self, parent)
        self.events = []
    
        # дизайн календаря
        self.setGridVisible(False)
        self.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setStyleSheet("""
        #qt_calendar_navigationbar {
    background-color: green;
    max-height: 48;
}
                           

    #qt_calendar_calendarview {
    outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
    selection-background-color: rgb(255, 255, 255); /* Выберите цвет фона */
}

    #qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none;                     /* убрать границу */
    margin-top: 12px;
    color: white;
    min-width: 36px;
    max-width: 72px;
    min-height: 36px;
    max-height: 72px;
    border-radius: 18px;            /* выглядит как эллипс */
    font-weight: bold;              /* шрифт полужирный    */
    font-size: 20px;
    
    /* Удалить стандартное изображение клавиши со стрелкой. 
       Вы также можете настроить                           */
    qproperty-icon: none;    
    background-color: transparent; /* Цвет фона прозрачный */
}
    #qt_calendar_prevmonth {
    qproperty-text: "<";         /* Изменить текст кнопки  */
    color: black;
}

    #qt_calendar_nextmonth {
    qproperty-text: ">";
    color: black;
}

    #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

CalendarWidget QToolButton::menu-indicator {
    image: none;      
    subcontrol-position: right center;              
}

/*  год, месяц                                                */
    #qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: black;
    margin: 6;
    min-width: 20px;
    border-radius: 16px;
                    
}

    #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года                                                        */
    #qt_calendar_yearedit {
    min-width: 50px;
    color: black;
    background: transparent;         /* Сделать фон окна ввода прозрачным */
}

    #qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */
    width: 24px;
    subcontrol-position: right;     
    
}

#qt_calendar_yearedit::down-button { /* Кнопка вниз     */
    width: 24px;
    subcontrol-position: left;
   
}

/* меню выбора месяца                                          */
CalendarWidget QToolButton QMenu {
    background-color: black;
}

CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}

CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}
                           
            """)


        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 16777214))
        

        # кастомайз субботы и воскресенья календаря
        fmtGreen = QTextCharFormat()
        fmtGreen.setForeground(QBrush(QColor(24, 214, 74)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Saturday, fmtGreen)
        fmtOrange = QTextCharFormat()
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Sunday, fmtOrange)

        hop = QTextCharFormat()
        hop.setForeground(QBrush(QColor(255, 0, 0)))
        self.setDateTextFormat(QtCore.QDate.currentDate(), hop)
    

    def paintCell(self, painter, rect, date):
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date == self.selectedDate():  
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.setBrush(QtGui.QColor(252, 0, 0, 100))  # последнее это прозрачность
            painter.drawEllipse(rect)


class MyCalendar(QCalendarWidget):

    def __init__(self, parent=None):
        QCalendarWidget.__init__(self, parent)
        self.events = []
    
        # дизайн календаря
        self.setGridVisible(False)
        self.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setStyleSheet("""
        #qt_calendar_navigationbar {
    background-color: rgb(255, 255, 0);
    max-height: 48;
}

    #qt_calendar_calendarview {
    outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
    selection-background-color: rgb(255, 255, 255); /* Выберите цвет фона */
}

    #qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none;                     /* убрать границу */
    margin-top: 12px;
    color: white;
    min-width: 36px;
    max-width: 72px;
    min-height: 36px;
    max-height: 72px;
    border-radius: 18px;            /* выглядит как эллипс */
    font-weight: bold;              /* шрифт полужирный    */
    font-size: 20px;
    
    /* Удалить стандартное изображение клавиши со стрелкой. 
       Вы также можете настроить                           */
    qproperty-icon: none;    
    background-color: transparent; /* Цвет фона прозрачный */
}
    #qt_calendar_prevmonth {
    qproperty-text: "<";         /* Изменить текст кнопки  */
    color: black;
}

    #qt_calendar_nextmonth {
    qproperty-text: ">";
    color: black;
}

    #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

CalendarWidget QToolButton::menu-indicator {
    image: none;      
    subcontrol-position: right center;              
}

/*  год, месяц                                                */
    #qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: black;
    margin: 6;
    min-width: 20px;
    border-radius: 16px;
}

    #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года                                                        */
    #qt_calendar_yearedit {
    min-width: 50px;
    color: black;
    background: transparent;         /* Сделать фон окна ввода прозрачным */
}

    #qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */
    width: 24px;
    subcontrol-position: right;     
    
}

#qt_calendar_yearedit::down-button { /* Кнопка вниз     */
    width: 24px;
    subcontrol-position: left;
   
}

/* меню выбора месяца                                          */
CalendarWidget QToolButton QMenu {
    background-color: black;
}

CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}

CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}



            """)


        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 16777214))
        

        # кастомайз субботы и воскресенья календаря
        fmtGreen = QTextCharFormat()
        fmtGreen.setForeground(QBrush(QColor(24, 214, 74)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Saturday, fmtGreen)
        fmtOrange = QTextCharFormat()
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Sunday, fmtOrange)

        hop = QTextCharFormat()
        hop.setForeground(QBrush(QColor(255, 0, 0)))
        self.setDateTextFormat(QtCore.QDate.currentDate(), hop)

        # получаем базы данных для рисования круглешков 
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        query = """SELECT data_create FROM hometask WHERE data_create != ''"""
        self.c = cursor.execute(query).fetchall()
        db.commit()
        self.g = []
        for i in range(len(list(self.c))):
            self.g.append(QDate(datetime.datetime.strptime(self.c[i][0], '%Y-%m-%d').date()))
        
       

    def paintCell(self, painter, rect, date):
        global cruk_size
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date == self.selectedDate():  
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.setBrush(QtGui.QColor(252, 0, 0, 100))  # последнее это прозрачность
            painter.drawEllipse(rect)
       
        if date in self.g:
            painter.setBrush(QColor(0, 255, 0))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawEllipse(rect.topRight() - QPoint(cruk_w, -cruk_h), cruk_size, cruk_size)
 

class create_calen_window(QMainWindow, QWidget):
    def __init__(self, parent=None):
        super(create_calen_window, self).__init__()
        loadUi('create_calen.ui', self)
        self.calendar = MyCalendar()
        self.setWindowIcon(QIcon('kalendar.png'))
        
        # добавляем кастомный календарь
        self.vl_kal.removeWidget(self.calendarWidget)
        self.vl_kal.removeWidget(self.gotovo_btn)
        self.vl_kal.addWidget(self.calendar)
        self.vl_kal.addWidget(self.gotovo_btn)
        self.calendarWidget.close()
  
        #self.calendarWidget.painter(drawEllipse, rect.topLeft() + QPoint(12, 7), 3, 3)

        # мелочи с интерфейсом
        self.gotovo_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); border-radius: 7px;  font: 18pt ; border: 3px; background-color: rgb(255,151,0);}"
                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: rgb(255, 255, 0);}"
                                      "QPushButton:pressed{background: rgb(0,0,0); color: red}")
        self.sost_lbl.setText("День не указан")

        self.predmert_box.setStyleSheet(""" QComboBox {
    border: 2px solid gray;
    border-radius: 6px;
    padding: 1px 18px 1px 3px;
    min-width: 6;
    color: black
}

QComboBox:editable {
    background: white;
}

QComboBox:!editable, QComboBox::drop-down:editable {
     background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);
}

/* QComboBox gets the "on" state when the popup is open */
QComboBox:!editable:on, QComboBox::drop-down:editable:on {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #D3D3D3, stop: 0.4 #D8D8D8,
                                stop: 0.5 #DDDDDD, stop: 1.0 #E1E1E1);
}

QComboBox:on { /* shift the text when the popup opens */
    padding-top: 3px;
    padding-left: 4px;
}

QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 0px;

    border-left-width: 1px;
    border-left-color: darkgray;
    border-left-style: solid; /* just a single line */
    border-top-right-radius: 3px; /* same radius as the QComboBox */
    border-bottom-right-radius: 3px;
}

QComboBox::down-arrow {
    color: black;
}

QComboBox::down-arrow:on { /* shift the arrow when popup is open */
    top: 1px;
    left: 1px;
}
QComboBox QAbstractItemView {
    border: 2px solid darkgray;
    selection-background-color: lightgray;
}

""")


        # сигналы
        self.gotovo_btn.clicked.connect(self.gotovo)
        self.calendar.clicked.connect(self.get_text_homework)



    def gotovo(self):
        create_calen_window.close()
        window.show()


    def get_text_homework(self):
        self.hwte.setText("")
        self.predmert_box.clear()
        self.sdacha_lbl.setText("")
        #self.predmert_box.setText("выберите предмет")
        # сравнимаем два календаря на даты
        self.data_now = self.calendar.selectedDate()
        self.data_now = self.data_now.toPyDate()
        
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()
        row = (self.data_now,)
        quary = """SELECT predmet, homework_text, data_sdachi FROM hometask WHERE data_create = ?"""  # дынные о предмете, о дз, о дате сдачи 
        quary_2 = """SELECT COUNT(predmet) FROM hometask WHERE data_create = ?""" # количество предметов на этот день
        y = cursor.execute(quary_2, row).fetchall()[0][0]  # выполняем что в предедкщие строке
        self.h = cursor.execute(quary, row).fetchall()
        # получили данные заполняем Qcombobox на предметы
        if y != 0:
            j = "Найдено " + str(y) + " ДЗ"
            self.sost_lbl.setText(j)
            for i in range(y):
                self.predmert_box.addItem(self.h[i][0])
        else:
            self.sost_lbl.setText("ДЗ не найдено")
        self.predmert_box.activated.connect(lambda: self.prov_in_predmet())

    # заполняем данные когда пользователь выьирает другой предмет в данном дне
    def prov_in_predmet(self):
        self.sdacha_lbl.setText("")
        self.hwte.setText(self.h[self.predmert_box.currentIndex()][1])
        if self.h[self.predmert_box.currentIndex()][2] != "":
            ne_h = str("Сдать до:  ") + str(self.h[self.predmert_box.currentIndex()][2])
            self.sdacha_lbl.setText(ne_h)
        else:
            self.sdacha_lbl.setText("Срок здачи не указан")


    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        global cruk_h, cruk_w, cruk_size
        # мастабирование и дизайн окна
        wsw = create_calen_window.width()
        wsh = create_calen_window.height()
        cal_wsw = int(wsw/100 *60)
        lbl_wsw = int(wsw - cal_wsw)
        otstup  = int(wsw/100 * 2)
        
        self.cal_w.resize(cal_wsw - otstup, wsh - otstup)
        self.lbl_w.resize(lbl_wsw - otstup, wsh - otstup)
        self.lbl_w.move(cal_wsw, 0)
        

        ws = wsw + wsh
     
        # расчитывем размер текста для всех объектов
        self.hw_font_func = QFont()
        self.sost_lbl_fonc_func = QFont()
        if ws > 1150:
            poi = int((ws-1150)//320)
            self.hw_font_func.setPointSize(14+poi)
            self.sost_lbl_fonc_func.setPointSize(14+poi)
        elif ws< 1150:
            poi_2 = int((ws-1150)//105)
            self.hw_font_func.setPointSize(14+poi_2)
            self.sost_lbl_fonc_func.setPointSize(14+poi_2)
        else:
            self.hw_font_func.setPointSize(14)
            self.sost_lbl_fonc_func.setPointSize(14)

        self.predmert_box_font_func = QFont()
        self.predmert_box_font_func.setPointSize(int(ws//64))
        
        self.gotovo_font_func = QFont()
        self.gotovo_font_func.setPointSize(int(ws//52.2))
        

        self.label_font_func = QFont()
        self.label_font_func.setPointSize(int(ws//44.2))
        
        
        
        self.cw_font_func = QFont()
        self.cw_font_func.setPointSize(int(ws//115))

        cruk_size = ws//304
        cruk_w = wsw//50
        cruk_h = wsh//35

        # задаем разер текста для всех обЪектов
        self.hwte.setFont(self.hw_font_func)
        self.predmert_box.setFont(self.predmert_box_font_func)
        self.sdacha_lbl.setFont(self.predmert_box_font_func)
        self.label.setFont(self.label_font_func)
        self.gotovo_btn.setFont(self.gotovo_font_func)
        self.sost_lbl.setFont(self.sost_lbl_fonc_func)
        self.calendar.setFont(self.cw_font_func)


    def closeEvent(self, event):
        self.hwte.setText("")
        self.predmert_box.clear()
        self.sdacha_lbl.setText("")


class nedavnee_vapol_window(QMainWindow, QWidget):
    def __init__(self):
        super(nedavnee_vapol_window, self).__init__()
        loadUi('nedavnie.ui', self)
        self.setMinimumSize(730, 310)
        self.setWindowTitle("недавно удаленные")
        win_icon = QIcon('nedavno_ydal_icon.png')
        self.setWindowIcon(win_icon)
        # переменные
        # 0 - выбрать
        # 1 - удалить
        # 2 - вернуть
        self.sost_btn = "2"
        self.sost_func = "vab"
        self.vabor_func = []

        # signal
        self.venutsa_btn.clicked.connect(lambda: self.vernutsa())
        self.vernut_btn.clicked.connect(self.vost_btn_event)
        self.delect_btn.clicked.connect(self.del_btn_event)

        # дизайн кнопок
        self.venutsa_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(255, 0, 255); border-radius: 12px; border: 2px;font: 75 22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
                                                      
        self.vernut_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(0, 170, 0); border-radius: 12px; border: 2px;font: 75 22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        
        self.delect_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(220, 0, 0); border-radius: 12px; border: 2px;font: 75 22pt 'MS Shell Dlg 2';}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
        self.twg.setFrameShape(QFrame.Shape.StyledPanel)
        self.twg.setFrameShadow(QFrame.Shadow.Plain)


    def create_table(self):
        self.twg.setRowCount(0)
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        jay = """SELECT COUNT(data_create) FROM nedavno_ydal"""

        cursor.execute(jay)

        db.commit()
        self.pasa = (cursor.fetchall()[0][0])

        for i in range(self.pasa):
            self.uni_btn = QPushButton("Вернуть", self)
            self.uni_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(0, 170, 0); border-radius: 12px; border: 2px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")

            if i + 1 > self.twg.rowCount():
                db = sqlite3.connect("htbase.db")
                cursor = db.cursor()
                query = """SELECT * from nedavno_ydal"""
                cursor.execute(query)
                arr = cursor.fetchall()  # доступ к базе данных по индексу

                db.commit()

                self.twg.setShowGrid(False)
                self.rowPosition = self.twg.rowCount()
                self.twg.insertRow(self.rowPosition)

               

                # заполняем табл
                self.twg.setCellWidget(self.rowPosition, 0, QLabel(arr[i][2], self))
                self.twg.setCellWidget(self.rowPosition, 1, QLabel(arr[i][3], self))
                self.twg.setCellWidget(self.rowPosition, 2, QLabel(arr[i][1], self))
                self.twg.setCellWidget(self.rowPosition, 3, QLabel(arr[i][0], self))
                self.twg.setCellWidget(self.rowPosition, 4, self.uni_btn)

                # сигналы
                self.uni_btn.clicked.connect(self.raspredel)
                

    def table_mashtab(self):
        curret_window_sizew = self.width()
        curret_window_sizeh = self.height()

        col_1 = int(curret_window_sizew/100 * 19)
        col_2 = int(curret_window_sizew/100 * 30)
        col_3 = int(curret_window_sizew/100 * 12)
        col_4 = int(curret_window_sizew/100 * 12)
        col_5 = int(curret_window_sizew - col_1 - col_2 - col_3 - col_4 - 30)

        self.twg.setColumnWidth(0, col_1)
        self.twg.setColumnWidth(1, col_2)
        self.twg.setColumnWidth(2, col_3)
        self.twg.setColumnWidth(3, col_4)
        self.twg.setColumnWidth(4, col_5)    
        

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:

        curret_window_sizew = self.width()
        curret_window_sizeh = self.height()
        self.venutsa_btn.setGeometry(10, 10, curret_window_sizew-20, int(curret_window_sizeh/100 * 15) - 10)
        self.btn_wid.setGeometry(10, int(curret_window_sizeh/100 * 15) + 5 + int(curret_window_sizeh/100 * 70), curret_window_sizew-20, int(curret_window_sizeh/100 * 15))
        self.twg.setGeometry(5, int(curret_window_sizeh/100 * 15) + 5, curret_window_sizew - 10, int(curret_window_sizeh/100 * 70) )
     
        self.table_mashtab()
       

    def vernutsa(self):
        nedavnee_vapol_window.close()
        window.show()
        window.create_table()


    def vost_btn_event(self):
        self.sost_func = "vost"
        if self.sost_btn == "0" or self.sost_btn == "1":
            self.sost_btn = "2"
            self.create_table_vost()
            

    def create_table_vost(self):
        self.twg.setRowCount(0)
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        jay = """SELECT COUNT(data_create) FROM nedavno_ydal"""

        cursor.execute(jay)

        db.commit()
        self.pasa = (cursor.fetchall()[0][0])
           
        for i in range(self.pasa):
            self.uni_btn = QPushButton("Вернуть", self)
            self.uni_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(0, 170, 0); border-radius: 12px; border: 2px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
            if i + 1 > self.twg.rowCount():
                db = sqlite3.connect("htbase.db")
                cursor = db.cursor()
                query = """SELECT * from nedavno_ydal"""
                cursor.execute(query)
                arr = cursor.fetchall()  # доступ к базе данных по индексу

                db.commit()

                self.twg.setShowGrid(False)
                self.rowPosition = self.twg.rowCount()
                self.twg.insertRow(self.rowPosition)

                

                # заполняем табл
                self.twg.setCellWidget(self.rowPosition, 0, QLabel(arr[i][2], self))
                self.twg.setCellWidget(self.rowPosition, 1, QLabel(arr[i][3], self))
                self.twg.setCellWidget(self.rowPosition, 2, QLabel(arr[i][1], self))
                self.twg.setCellWidget(self.rowPosition, 3, QLabel(arr[i][0], self))
                self.twg.setCellWidget(self.rowPosition, 4, self.uni_btn)

                # сигналы
                self.uni_btn.clicked.connect(self.raspredel)


    def del_btn_event(self):
        self.sost_func = "del"
        self.sost_btn = "1"
        self.del_create_table()

    
    def del_create_table(self):
        self.twg.setRowCount(0)
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        jay = """SELECT COUNT(data_create) FROM nedavno_ydal"""

        cursor.execute(jay)

        db.commit()
        self.pasa = (cursor.fetchall()[0][0])
           
        for i in range(self.pasa):
            self.uni_btn = QPushButton("Удалить", self)
            self.uni_btn.setStyleSheet("QPushButton{color: rgb(0, 0, 0); background-color: rgb(220, 0, 0); border-radius: 12px; border: 2px;}"
                                                      "QPushButton:hover{color: rgb(47, 255, 168); background-color: grey;}"
                                                      "QPushButton:pressed{background: solid grey; color:solid grey}""")
            if i + 1 > self.twg.rowCount():
                db = sqlite3.connect("htbase.db")
                cursor = db.cursor()
                query = """SELECT * from nedavno_ydal"""
                cursor.execute(query)
                arr = cursor.fetchall()  # доступ к базе данных по индексу

                db.commit()

                self.twg.setShowGrid(False)
                self.rowPosition = self.twg.rowCount()
                self.twg.insertRow(self.rowPosition)

                

                # заполняем табл
                self.twg.setCellWidget(self.rowPosition, 0, QLabel(arr[i][2], self))
                self.twg.setCellWidget(self.rowPosition, 1, QLabel(arr[i][3], self))
                self.twg.setCellWidget(self.rowPosition, 2, QLabel(arr[i][1], self))
                self.twg.setCellWidget(self.rowPosition, 3, QLabel(arr[i][0], self))
                self.twg.setCellWidget(self.rowPosition, 4, self.uni_btn)

                # сигналы
                self.uni_btn.clicked.connect(self.raspredel)


    def raspredel(self):
        if self.sost_btn == "1":
            self.delect()
        elif self.sost_btn =="2":
            self.vost()


    def vost(self):
        # алгоритм востановления
        crow = self.twg.currentRow()
        bb = (int(crow+1),)
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()

        m = """DELETE FROM nedavno_ydal WHERE rowid = ? """
        dek = """SELECT * FROM nedavno_ydal WHERE rowid =?"""
        up = """INSERT INTO hometask(data_create, data_sdachi, homework_text, predmet) VALUES(?,?,?,?)"""
        vac = """VACUUM"""
        cursor.execute(vac)

        n = cursor.execute(dek, bb).fetchall()
        up_box = n[0][0], n[0][1], n[0][3], n[0][2]
        cursor.execute(up, up_box)
        cursor.execute(m, bb)


        db.commit()
        self.twg.removeRow(crow)


    def delect(self):
        # алгоритм удаления 
        crow = self.twg.currentRow()
        bb = (int(crow+1),)
        db = sqlite3.connect('htbase.db')
        cursor = db.cursor()

        m = """DELETE FROM nedavno_ydal WHERE rowid = ? """
        j = """SELECT rowid FROM hometask"""
        dek = """SELECT * FROM hometask WHERE rowid =?"""
        vac = """VACUUM"""
        cursor.execute(vac)

        n = cursor.execute(dek, bb).fetchall()
        cursor.execute(m, bb)

        db.commit()
        self.twg.removeRow(crow)


class BaseCustomCalendar_y(QCalendarWidget):

    def __init__(self, parent=None):
        QCalendarWidget.__init__(self, parent)
        self.events = []
    
        # дизайн календаря
        self.setGridVisible(False)
        self.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setStyleSheet("""
        #qt_calendar_navigationbar {
    background-color: rgb(255, 255, 0);
    max-height: 48;
}

    #qt_calendar_calendarview {
    outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
    selection-background-color: rgba(255, 255, 255, 0); /* Выберите цвет фона */
    
}

    #qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none;                     /* убрать границу */
    margin-top: 12px;
    color: white;
    min-width: 36px;
    max-width: 72px;
    min-height: 36px;
    max-height: 72px;
    border-radius: 18px;            /* выглядит как эллипс */
    font-weight: bold;              /* шрифт полужирный    */
    font-size: 20px;
    
    /* Удалить стандартное изображение клавиши со стрелкой. 
       Вы также можете настроить                           */
    qproperty-icon: none;    
    background-color: transparent; /* Цвет фона прозрачный */
}
    #qt_calendar_prevmonth {
    qproperty-text: "<";         /* Изменить текст кнопки  */
    color: black;
}

    #qt_calendar_nextmonth {
    qproperty-text: ">";
    color: black;
}

    #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

CalendarWidget QToolButton::menu-indicator {
    image: none;      
    subcontrol-position: right center;              
}

/*  год, месяц                                                */
    #qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: black;
    margin: 6;
    min-width: 20px;
    border-radius: 16px;
}

    #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года                                                        */
    #qt_calendar_yearedit {
    min-width: 50px;
    color: black;
    background: transparent;         /* Сделать фон окна ввода прозрачным */
}

    #qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */
    width: 24px;
    subcontrol-position: right;     
    
}

#qt_calendar_yearedit::down-button { /* Кнопка вниз     */
    width: 24px;
    subcontrol-position: left;
   
}

/* меню выбора месяца                                          */
CalendarWidget QToolButton QMenu {
    background-color: black;
}

CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}

CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}



            """)


        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 16777214))
        

        # кастомайз субботы и воскресенья календаря
        fmtGreen = QTextCharFormat()
        fmtGreen.setForeground(QBrush(QColor(24, 214, 74)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Saturday, fmtGreen)
        fmtOrange = QTextCharFormat()
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Sunday, fmtOrange)

        hop = QTextCharFormat()
        hop.setForeground(QBrush(QColor(255, 0, 0)))
        self.setDateTextFormat(QtCore.QDate.currentDate(), hop)
    

    def paintCell(self, painter, rect, date):
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date == self.selectedDate():  
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.setBrush(QtGui.QColor(235, 0, 0, 100))
            #centre = rect.center()
            #if rect.height() > rect.width():
                #rasn = rect.height() - rect.width()
                #rect.moveCenter(rect.center() + rect.width())
                #rect.setTop(rect.top() + int(rasn/2)*5)
                #rect.setHeight(rect.width())
            #else:
                #rasn = rect.width() - rect.height()
                #rect.setWidth(rect.height())
                #rect.setLeft(rect.left() + int(rasn))
            
            #print(rect.center())
            #print(rect)
            #print(rect.right(), rect.bottom())  # последнее это прозрачность
            painter.drawEllipse(rect)


class MyCalendar_S(QCalendarWidget):

    def __init__(self, parent=None):
        QCalendarWidget.__init__(self, parent)
        self.events = []
    
        # дизайн календаря
        self.setGridVisible(False)
        self.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.SingleSelection)
        self.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        self.setStyleSheet("""
        #qt_calendar_navigationbar {
    background-color: rgb(255, 255, 0);
    max-height: 48;
}

    #qt_calendar_calendarview {
    outline: 0px;                                 /* Удалить выделенную пунктирную рамку */
    selection-background-color: rgb(255, 255, 255); /* Выберите цвет фона */
}

    #qt_calendar_prevmonth, #qt_calendar_nextmonth {
    border: none;                     /* убрать границу */
    margin-top: 12px;
    color: white;
    min-width: 36px;
    max-width: 72px;
    min-height: 36px;
    max-height: 72px;
    border-radius: 18px;            /* выглядит как эллипс */
    font-weight: bold;              /* шрифт полужирный    */
    font-size: 20px;
    
    /* Удалить стандартное изображение клавиши со стрелкой. 
       Вы также можете настроить                           */
    qproperty-icon: none;    
    background-color: transparent; /* Цвет фона прозрачный */
}
    #qt_calendar_prevmonth {
    qproperty-text: "<";         /* Изменить текст кнопки  */
    color: black;
}

    #qt_calendar_nextmonth {
    qproperty-text: ">";
    color: black;
}

    #qt_calendar_prevmonth:hover, #qt_calendar_nextmonth:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_prevmonth:pressed, #qt_calendar_nextmonth:pressed {
    background-color: rgba(235, 235, 235, 100);
}

CalendarWidget QToolButton::menu-indicator {
    image: none;      
    subcontrol-position: right center;              
}

/*  год, месяц                                                */
    #qt_calendar_yearbutton, #qt_calendar_monthbutton {
    color: black;
    margin: 6;
    min-width: 20px;
    border-radius: 16px;
}

    #qt_calendar_yearbutton:hover, #qt_calendar_monthbutton:hover {
    background-color: rgba(225, 225, 225, 100);
}

    #qt_calendar_yearbutton:pressed, #qt_calendar_monthbutton:pressed {
    background-color: rgba(235, 235, 235, 100);
}

/* Поле ввода года                                                        */
    #qt_calendar_yearedit {
    min-width: 50px;
    color: black;
    background: transparent;         /* Сделать фон окна ввода прозрачным */
}

    #qt_calendar_yearedit::up-button {   /* Кнопка вверх                      */
    width: 24px;
    subcontrol-position: right;     
    
}

#qt_calendar_yearedit::down-button { /* Кнопка вниз     */
    width: 24px;
    subcontrol-position: left;
   
}

/* меню выбора месяца                                          */
CalendarWidget QToolButton QMenu {
    background-color: black;
}

CalendarWidget QToolButton QMenu::item {
    padding: 10px;
}

CalendarWidget QToolButton QMenu::item:selected:enabled {
    background-color: rgb(230, 230, 230);
}



            """)


        self.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 16777214))
        

        # кастомайз субботы и воскресенья календаря
        fmtGreen = QTextCharFormat()
        fmtGreen.setForeground(QBrush(QColor(24, 214, 74)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Saturday, fmtGreen)
        fmtOrange = QTextCharFormat()
        fmtOrange.setForeground(QBrush(QColor(252, 140, 28)))
        self.setWeekdayTextFormat(QtCore.Qt.DayOfWeek.Sunday, fmtOrange)

        hop = QTextCharFormat()
        hop.setForeground(QBrush(QColor(255, 0, 0)))
        self.setDateTextFormat(QtCore.QDate.currentDate(), hop)

        # получаем базы данных для рисования круглешков 
        
        db = sqlite3.connect("htbase.db")
        cursor = db.cursor()
        query = """SELECT data_sdachi FROM hometask WHERE data_sdachi != '' """
        self.c = cursor.execute(query).fetchall()
        db.commit()
        self.g = []
        for i in range(len(list(self.c))):
            b = datetime.datetime.strptime(self.c[i][0], '%Y-%m-%d').date()
            self.g.append(QtCore.QDate(b))
        
       

    def paintCell(self, painter, rect, date):
        global cruk_size
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date == self.selectedDate():  
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.setBrush(QtGui.QColor(252, 0, 0, 100))  # последнее это прозрачность
            painter.drawEllipse(rect)
       
        if date in self.g:
            painter.setBrush(QColor(0, 255, 0))
            painter.setPen(QtGui.QColor(0, 0, 0, 0))
            painter.drawEllipse(rect.topRight() - QPoint(cruk_w, -cruk_h), cruk_size, cruk_size)
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sdacha_calen_window = sdacha_calen_window()
    create_calen_window = create_calen_window()
    nedavnee_vapol_window = nedavnee_vapol_window()
    create_Homework = create_Homework()
    cell_click = cell_click()
    window = MainWindow()
    window.show()
    app.exec()
