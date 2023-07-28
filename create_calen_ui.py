# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_calen.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QFrame,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(676, 449)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QSize(459, 275))
        mainWindow.setWindowOpacity(5.000000000000000)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbl_w = QWidget(self.centralwidget)
        self.lbl_w.setObjectName(u"lbl_w")
        self.lbl_w.setGeometry(QRect(350, 0, 301, 451))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_w.sizePolicy().hasHeightForWidth())
        self.lbl_w.setSizePolicy(sizePolicy1)
        self.lbl_w.setMinimumSize(QSize(0, 0))
        self.lbl_w.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout = QVBoxLayout(self.lbl_w)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(2, 5, 2, 0)
        self.sost_lbl = QLabel(self.lbl_w)
        self.sost_lbl.setObjectName(u"sost_lbl")
        sizePolicy1.setHeightForWidth(self.sost_lbl.sizePolicy().hasHeightForWidth())
        self.sost_lbl.setSizePolicy(sizePolicy1)
        self.sost_lbl.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.sost_lbl.setFont(font)
        self.sost_lbl.setStyleSheet(u"")
        self.sost_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.sost_lbl)

        self.predmert_box = QComboBox(self.lbl_w)
        self.predmert_box.setObjectName(u"predmert_box")
        sizePolicy1.setHeightForWidth(self.predmert_box.sizePolicy().hasHeightForWidth())
        self.predmert_box.setSizePolicy(sizePolicy1)
        self.predmert_box.setMinimumSize(QSize(0, 0))
        self.predmert_box.setMaximumSize(QSize(16777215, 60))
        self.predmert_box.setSizeIncrement(QSize(0, 0))
        self.predmert_box.setBaseSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.predmert_box.setFont(font1)
        self.predmert_box.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.predmert_box)

        self.hwte = QTextEdit(self.lbl_w)
        self.hwte.setObjectName(u"hwte")
        self.hwte.setStyleSheet(u"\n"
"color: rgb(255, 170, 0);")
        self.hwte.setFrameShape(QFrame.StyledPanel)
        self.hwte.setFrameShadow(QFrame.Plain)
        self.hwte.setLineWidth(1)
        self.hwte.setMidLineWidth(0)
        self.hwte.setUndoRedoEnabled(True)
        self.hwte.setReadOnly(True)
        self.hwte.setTabStopDistance(81.000000000000000)

        self.verticalLayout.addWidget(self.hwte)

        self.sdacha_lbl = QLabel(self.lbl_w)
        self.sdacha_lbl.setObjectName(u"sdacha_lbl")
        sizePolicy1.setHeightForWidth(self.sdacha_lbl.sizePolicy().hasHeightForWidth())
        self.sdacha_lbl.setSizePolicy(sizePolicy1)
        self.sdacha_lbl.setMaximumSize(QSize(16777215, 60))
        self.sdacha_lbl.setFont(font1)
        self.sdacha_lbl.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.sdacha_lbl)

        self.cal_w = QWidget(self.centralwidget)
        self.cal_w.setObjectName(u"cal_w")
        self.cal_w.setGeometry(QRect(10, 10, 301, 391))
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cal_w.sizePolicy().hasHeightForWidth())
        self.cal_w.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.cal_w)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.vl_kal = QVBoxLayout()
        self.vl_kal.setSpacing(2)
        self.vl_kal.setObjectName(u"vl_kal")
        self.vl_kal.setContentsMargins(-1, -1, -1, 0)
        self.label = QLabel(self.cal_w)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(26)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"\n"
"color: rgb(170, 85, 255);")

        self.vl_kal.addWidget(self.label)

        self.calendarWidget = QCalendarWidget(self.cal_w)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(50)
        sizePolicy3.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy3)
        self.calendarWidget.setMaximumSize(QSize(16777215, 16777214))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.calendarWidget.setFont(font3)
        self.calendarWidget.setMouseTracking(False)
        self.calendarWidget.setTabletTracking(False)
        self.calendarWidget.setFocusPolicy(Qt.NoFocus)
        self.calendarWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.calendarWidget.setAcceptDrops(False)
        self.calendarWidget.setToolTipDuration(0)
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(False)
        self.calendarWidget.setStyleSheet(u"selection-background-color: rgb(255, 255, 0);\n"
"\n"
"selection-color: rgb(0, 0, 0);\n"
"")
        self.calendarWidget.setInputMethodHints(Qt.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setDateEditAcceptDelay(1500)

        self.vl_kal.addWidget(self.calendarWidget)

        self.gotovo_btn = QPushButton(self.cal_w)
        self.gotovo_btn.setObjectName(u"gotovo_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(7)
        sizePolicy4.setHeightForWidth(self.gotovo_btn.sizePolicy().hasHeightForWidth())
        self.gotovo_btn.setSizePolicy(sizePolicy4)
        self.gotovo_btn.setMaximumSize(QSize(16777215, 16777214))
        self.gotovo_btn.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Niagara Engraved"])
        font4.setPointSize(1)
        font4.setBold(False)
        font4.setItalic(False)
        self.gotovo_btn.setFont(font4)
        self.gotovo_btn.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255,151,0);\n"
"border-radius: 12px; \n"
"border: 3px;\n"
"\n"
"")

        self.vl_kal.addWidget(self.gotovo_btn)


        self.verticalLayout_2.addLayout(self.vl_kal)

        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)

        self.predmert_box.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"\u041a\u0430\u043b\u0435\u043d\u0434\u0430\u0440\u044c \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u044f", None))
        self.sost_lbl.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.hwte.setHtml(QCoreApplication.translate("mainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.sdacha_lbl.setText("")
        self.label.setText(QCoreApplication.translate("mainWindow", u"<html><head/><body><p align=\"center\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0435\u043d\u044c \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f </p></body></html>", None))
        self.gotovo_btn.setText(QCoreApplication.translate("mainWindow", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

