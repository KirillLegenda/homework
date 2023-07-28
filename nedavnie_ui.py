# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nedavnie.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 565)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.venutsa_btn = QPushButton(self.centralwidget)
        self.venutsa_btn.setObjectName(u"venutsa_btn")
        self.venutsa_btn.setGeometry(QRect(9, 9, 801, 61))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.venutsa_btn.sizePolicy().hasHeightForWidth())
        self.venutsa_btn.setSizePolicy(sizePolicy1)
        self.venutsa_btn.setSizeIncrement(QSize(0, 0))
        self.venutsa_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 255);\n"
"border: 2px;\n"
"border-radius: 8px;")
        self.twg = QTableWidget(self.centralwidget)
        if (self.twg.columnCount() < 5):
            self.twg.setColumnCount(5)
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.twg.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.twg.setObjectName(u"twg")
        self.twg.setGeometry(QRect(10, 80, 791, 401))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.twg.sizePolicy().hasHeightForWidth())
        self.twg.setSizePolicy(sizePolicy2)
        self.twg.setMaximumSize(QSize(16777214, 16777215))
        self.twg.setSizeIncrement(QSize(600, 600))
        self.twg.setFocusPolicy(Qt.TabFocus)
        self.twg.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"selection-color: rgb(255, 0, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"")
        self.twg.setFrameShape(QFrame.StyledPanel)
        self.twg.setFrameShadow(QFrame.Plain)
        self.twg.setLineWidth(1)
        self.twg.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.twg.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.twg.horizontalHeader().setMinimumSectionSize(0)
        self.twg.verticalHeader().setMinimumSectionSize(27)
        self.twg.verticalHeader().setDefaultSectionSize(30)
        self.btn_wid = QWidget(self.centralwidget)
        self.btn_wid.setObjectName(u"btn_wid")
        self.btn_wid.setGeometry(QRect(0, 480, 821, 91))
        sizePolicy2.setHeightForWidth(self.btn_wid.sizePolicy().hasHeightForWidth())
        self.btn_wid.setSizePolicy(sizePolicy2)
        self.btn_wid.setFocusPolicy(Qt.NoFocus)
        self.btn_wid.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(self.btn_wid)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.vernut_btn = QPushButton(self.btn_wid)
        self.vernut_btn.setObjectName(u"vernut_btn")
        sizePolicy2.setHeightForWidth(self.vernut_btn.sizePolicy().hasHeightForWidth())
        self.vernut_btn.setSizePolicy(sizePolicy2)
        self.vernut_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(0, 170, 0);\n"
"border: 2px;\n"
"border-radius: 8px;")

        self.horizontalLayout.addWidget(self.vernut_btn)

        self.delect_btn = QPushButton(self.btn_wid)
        self.delect_btn.setObjectName(u"delect_btn")
        self.delect_btn.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.delect_btn.sizePolicy().hasHeightForWidth())
        self.delect_btn.setSizePolicy(sizePolicy2)
        self.delect_btn.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.delect_btn.setFont(font)
        self.delect_btn.setLayoutDirection(Qt.LeftToRight)
        self.delect_btn.setAutoFillBackground(False)
        self.delect_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 75 22pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 0, 0);\n"
"border: 2px;\n"
"border-radius: 8px;")
        self.delect_btn.setCheckable(True)
        self.delect_btn.setChecked(True)
        self.delect_btn.setAutoRepeatDelay(300)

        self.horizontalLayout.addWidget(self.delect_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.venutsa_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u0441\u044f", None))
        ___qtablewidgetitem = self.twg.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u043c\u0435\u0442", None));
        ___qtablewidgetitem1 = self.twg.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435", None));
        ___qtablewidgetitem2 = self.twg.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0440\u043e\u043a", None));
        ___qtablewidgetitem3 = self.twg.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u043d\u043e", None));
        self.vernut_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c", None))
        self.delect_btn.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

