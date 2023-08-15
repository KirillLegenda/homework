# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homework.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(524, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(6)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.create_Homework_btn = QPushButton(self.widget)
        self.create_Homework_btn.setObjectName(u"create_Homework_btn")
        self.create_Homework_btn.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(7)
        sizePolicy2.setHeightForWidth(self.create_Homework_btn.sizePolicy().hasHeightForWidth())
        self.create_Homework_btn.setSizePolicy(sizePolicy2)
        self.create_Homework_btn.setMaximumSize(QSize(16777215, 16777215))
        self.create_Homework_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 33);\n"
"border: 2px;\n"
"border-radius: 8px;")
        self.create_Homework_btn.setCheckable(True)
        self.create_Homework_btn.setChecked(False)

        self.horizontalLayout.addWidget(self.create_Homework_btn)

        self.btn_create_calen = QPushButton(self.widget)
        self.btn_create_calen.setObjectName(u"btn_create_calen")
        self.btn_create_calen.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_create_calen.sizePolicy().hasHeightForWidth())
        self.btn_create_calen.setSizePolicy(sizePolicy2)
        self.btn_create_calen.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.btn_create_calen.setFont(font)
        self.btn_create_calen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 33);\n"
"border: 2px;\n"
"border-radius: 8px;")
        self.btn_create_calen.setCheckable(True)
        self.btn_create_calen.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_create_calen)

        self.btn_sdaci_calen = QPushButton(self.widget)
        self.btn_sdaci_calen.setObjectName(u"btn_sdaci_calen")
        self.btn_sdaci_calen.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_sdaci_calen.sizePolicy().hasHeightForWidth())
        self.btn_sdaci_calen.setSizePolicy(sizePolicy2)
        self.btn_sdaci_calen.setMaximumSize(QSize(16777215, 16777215))
        self.btn_sdaci_calen.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 33);\n"
"border: 2px;\n"
"border-radius: 8px;")
        self.btn_sdaci_calen.setCheckable(True)
        self.btn_sdaci_calen.setChecked(False)

        self.horizontalLayout.addWidget(self.btn_sdaci_calen)


        self.verticalLayout.addWidget(self.widget)

        self.str_o = QComboBox(self.centralwidget)
        self.str_o.addItem("")
        self.str_o.addItem("")
        self.str_o.addItem("")
        self.str_o.addItem("")
        self.str_o.setObjectName(u"str_o")
        self.str_o.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(3)
        sizePolicy3.setHeightForWidth(self.str_o.sizePolicy().hasHeightForWidth())
        self.str_o.setSizePolicy(sizePolicy3)
        self.str_o.setStyleSheet(u"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 0);")
        self.str_o.setEditable(False)
        self.str_o.setFrame(True)

        self.verticalLayout.addWidget(self.str_o)

        self.twg = QTableWidget(self.centralwidget)
        if (self.twg.columnCount() < 4):
            self.twg.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.twg.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.twg.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.twg.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.twg.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.twg.setObjectName(u"twg")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(55)
        sizePolicy4.setHeightForWidth(self.twg.sizePolicy().hasHeightForWidth())
        self.twg.setSizePolicy(sizePolicy4)
        self.twg.setAutoFillBackground(False)
        self.twg.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.twg.setFrameShape(QFrame.NoFrame)
        self.twg.setFrameShadow(QFrame.Plain)
        self.twg.setLineWidth(0)
        self.twg.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.twg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.twg.setShowGrid(True)
        self.twg.setGridStyle(Qt.DotLine)
        self.twg.setRowCount(0)
        self.twg.horizontalHeader().setVisible(True)
        self.twg.horizontalHeader().setCascadingSectionResizes(False)
        self.twg.horizontalHeader().setProperty("showSortIndicator", False)
        self.twg.horizontalHeader().setStretchLastSection(True)
        self.twg.verticalHeader().setProperty("showSortIndicator", False)
        self.twg.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.twg)

        self.btn_nedavnii = QPushButton(self.centralwidget)
        self.btn_nedavnii.setObjectName(u"btn_nedavnii")
        sizePolicy1.setHeightForWidth(self.btn_nedavnii.sizePolicy().hasHeightForWidth())
        self.btn_nedavnii.setSizePolicy(sizePolicy1)
        self.btn_nedavnii.setStyleSheet(u"color: rgb(255, 170, 0);\n"
"font: 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(241, 0, 0);")

        self.verticalLayout.addWidget(self.btn_nedavnii)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menanger", None))
        self.create_Homework_btn.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0414\u0417", None))
        self.btn_create_calen.setText(QCoreApplication.translate("MainWindow", u"create_calen", None))
        self.btn_sdaci_calen.setText(QCoreApplication.translate("MainWindow", u"sdachi_calen", None))
        self.str_o.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c  \u043f\u043e \u0434\u0430\u0442\u0435 \u0441\u0434\u0430\u0447\u0438", None))
        self.str_o.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0434\u0430\u0442\u0435 \u0441\u0434\u0430\u0447\u0438(\u043e\u0431\u0440\u0430\u0442\u043d\u0430\u044f)", None))
        self.str_o.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u0434\u0430\u0442\u0435 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.str_o.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043f\u043e \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u0443 \u0414\u0417", None))

        ___qtablewidgetitem = self.twg.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None));
        ___qtablewidgetitem1 = self.twg.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem2 = self.twg.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None));
        ___qtablewidgetitem3 = self.twg.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None));
        self.btn_nedavnii.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0434\u0430\u0432\u043d\u043e \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435 ", None))
    # retranslateUi

