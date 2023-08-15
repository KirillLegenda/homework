# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cell_dia.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QComboBox, QDialog,
    QFrame, QLabel, QLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(685, 454)
        self.lbl_w = QWidget(Dialog)
        self.lbl_w.setObjectName(u"lbl_w")
        self.lbl_w.setGeometry(QRect(350, 10, 301, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_w.sizePolicy().hasHeightForWidth())
        self.lbl_w.setSizePolicy(sizePolicy)
        self.lbl_w.setMinimumSize(QSize(0, 0))
        self.lbl_w.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_7 = QVBoxLayout(self.lbl_w)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_7.setContentsMargins(2, 5, 2, 0)
        self.sost_lbl_4 = QLabel(self.lbl_w)
        self.sost_lbl_4.setObjectName(u"sost_lbl_4")
        sizePolicy.setHeightForWidth(self.sost_lbl_4.sizePolicy().hasHeightForWidth())
        self.sost_lbl_4.setSizePolicy(sizePolicy)
        self.sost_lbl_4.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamilies([u"Myanmar Text"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.sost_lbl_4.setFont(font)
        self.sost_lbl_4.setStyleSheet(u"")
        self.sost_lbl_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.sost_lbl_4)

        self.predmert_box_4 = QComboBox(self.lbl_w)
        self.predmert_box_4.setObjectName(u"predmert_box_4")
        sizePolicy.setHeightForWidth(self.predmert_box_4.sizePolicy().hasHeightForWidth())
        self.predmert_box_4.setSizePolicy(sizePolicy)
        self.predmert_box_4.setMinimumSize(QSize(0, 0))
        self.predmert_box_4.setMaximumSize(QSize(16777215, 60))
        self.predmert_box_4.setSizeIncrement(QSize(0, 0))
        self.predmert_box_4.setBaseSize(QSize(0, 20))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setItalic(False)
        self.predmert_box_4.setFont(font1)
        self.predmert_box_4.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.predmert_box_4)

        self.hwte_4 = QTextEdit(self.lbl_w)
        self.hwte_4.setObjectName(u"hwte_4")
        self.hwte_4.setStyleSheet(u"\n"
"color: rgb(255, 170, 0);")
        self.hwte_4.setFrameShape(QFrame.StyledPanel)
        self.hwte_4.setFrameShadow(QFrame.Plain)
        self.hwte_4.setLineWidth(1)
        self.hwte_4.setMidLineWidth(0)
        self.hwte_4.setUndoRedoEnabled(True)
        self.hwte_4.setReadOnly(True)
        self.hwte_4.setTabStopDistance(81.000000000000000)

        self.verticalLayout_7.addWidget(self.hwte_4)

        self.sdacha_lbl_4 = QLabel(self.lbl_w)
        self.sdacha_lbl_4.setObjectName(u"sdacha_lbl_4")
        sizePolicy.setHeightForWidth(self.sdacha_lbl_4.sizePolicy().hasHeightForWidth())
        self.sdacha_lbl_4.setSizePolicy(sizePolicy)
        self.sdacha_lbl_4.setMaximumSize(QSize(16777215, 60))
        self.sdacha_lbl_4.setFont(font1)
        self.sdacha_lbl_4.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.sdacha_lbl_4)

        self.cal_w = QWidget(Dialog)
        self.cal_w.setObjectName(u"cal_w")
        self.cal_w.setGeometry(QRect(10, 20, 301, 391))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cal_w.sizePolicy().hasHeightForWidth())
        self.cal_w.setSizePolicy(sizePolicy1)
        self.verticalLayout_8 = QVBoxLayout(self.cal_w)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.vl_kal_4 = QVBoxLayout()
        self.vl_kal_4.setSpacing(2)
        self.vl_kal_4.setObjectName(u"vl_kal_4")
        self.vl_kal_4.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(self.cal_w)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(26)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"\n"
"color: rgb(170, 85, 255);")

        self.vl_kal_4.addWidget(self.label_4)

        self.calendarWidget_4 = QCalendarWidget(self.cal_w)
        self.calendarWidget_4.setObjectName(u"calendarWidget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(50)
        sizePolicy2.setHeightForWidth(self.calendarWidget_4.sizePolicy().hasHeightForWidth())
        self.calendarWidget_4.setSizePolicy(sizePolicy2)
        self.calendarWidget_4.setMaximumSize(QSize(16777215, 16777214))
        font3 = QFont()
        font3.setFamilies([u"MS Shell Dlg 2"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.calendarWidget_4.setFont(font3)
        self.calendarWidget_4.setMouseTracking(False)
        self.calendarWidget_4.setTabletTracking(False)
        self.calendarWidget_4.setFocusPolicy(Qt.NoFocus)
        self.calendarWidget_4.setContextMenuPolicy(Qt.NoContextMenu)
        self.calendarWidget_4.setAcceptDrops(False)
        self.calendarWidget_4.setToolTipDuration(0)
        self.calendarWidget_4.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget_4.setAutoFillBackground(False)
        self.calendarWidget_4.setStyleSheet(u"selection-background-color: rgb(255, 255, 0);\n"
"\n"
"selection-color: rgb(0, 0, 0);\n"
"")
        self.calendarWidget_4.setInputMethodHints(Qt.ImhNone)
        self.calendarWidget_4.setFirstDayOfWeek(Qt.Monday)
        self.calendarWidget_4.setGridVisible(False)
        self.calendarWidget_4.setSelectionMode(QCalendarWidget.SingleSelection)
        self.calendarWidget_4.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.calendarWidget_4.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_4.setNavigationBarVisible(True)
        self.calendarWidget_4.setDateEditEnabled(False)
        self.calendarWidget_4.setDateEditAcceptDelay(1500)

        self.vl_kal_4.addWidget(self.calendarWidget_4)

        self.gotovo_btn_4 = QPushButton(self.cal_w)
        self.gotovo_btn_4.setObjectName(u"gotovo_btn_4")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(7)
        sizePolicy3.setHeightForWidth(self.gotovo_btn_4.sizePolicy().hasHeightForWidth())
        self.gotovo_btn_4.setSizePolicy(sizePolicy3)
        self.gotovo_btn_4.setMaximumSize(QSize(16777215, 16777214))
        self.gotovo_btn_4.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Niagara Engraved"])
        font4.setPointSize(1)
        font4.setBold(False)
        font4.setItalic(False)
        self.gotovo_btn_4.setFont(font4)
        self.gotovo_btn_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255,151,0);\n"
"border-radius: 12px; \n"
"border: 3px;\n"
"\n"
"")

        self.vl_kal_4.addWidget(self.gotovo_btn_4)


        self.verticalLayout_8.addLayout(self.vl_kal_4)


        self.retranslateUi(Dialog)

        self.predmert_box_4.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.sost_lbl_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p><p><br/></p></body></html>", None))
        self.hwte_4.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>", None))
        self.sdacha_lbl_4.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0434\u0435\u043d\u044c </p></body></html>", None))
        self.gotovo_btn_4.setText(QCoreApplication.translate("Dialog", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
    # retranslateUi

