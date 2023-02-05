# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Script_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(927, 642)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Box)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 120))
        self.frame_2.setMaximumSize(QtCore.QSize(150, 120))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonViewAllMarkets = QtWidgets.QPushButton(self.frame_2)
        self.ButtonViewAllMarkets.setMinimumSize(QtCore.QSize(100, 50))
        self.ButtonViewAllMarkets.setObjectName("ButtonViewAllMarkets")
        self.verticalLayout.addWidget(self.ButtonViewAllMarkets)
        self.ButtonFindMarkets = QtWidgets.QPushButton(self.frame_2)
        self.ButtonFindMarkets.setMinimumSize(QtCore.QSize(50, 50))
        self.ButtonFindMarkets.setObjectName("ButtonFindMarkets")
        self.verticalLayout.addWidget(self.ButtonFindMarkets)
        self.gridLayout_3.addWidget(self.frame_2, 0, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.MarketTable = QtWidgets.QTableWidget(self.page)
        self.MarketTable.setMinimumSize(QtCore.QSize(0, 0))
        self.MarketTable.setObjectName("MarketTable")
        self.MarketTable.setColumnCount(0)
        self.MarketTable.setRowCount(0)
        self.gridLayout_3.addWidget(self.MarketTable, 1, 0, 1, 4)
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(175, 120))
        self.frame_3.setMaximumSize(QtCore.QSize(175, 120))
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(175, 40))
        self.label.setMaximumSize(QtCore.QSize(175, 400))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setMinimumSize(QtCore.QSize(175, 30))
        self.widget.setMaximumSize(QtCore.QSize(175, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.inputFmid = QtWidgets.QTextEdit(self.widget)
        self.inputFmid.setMinimumSize(QtCore.QSize(110, 30))
        self.inputFmid.setMaximumSize(QtCore.QSize(110, 30))
        self.inputFmid.setObjectName("inputFmid")
        self.horizontalLayout_4.addWidget(self.inputFmid)
        self.verticalLayout_2.addWidget(self.widget)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setMinimumSize(QtCore.QSize(175, 50))
        self.frame_4.setMaximumSize(QtCore.QSize(175, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ButtonViewWriteReviews = QtWidgets.QPushButton(self.frame_4)
        self.ButtonViewWriteReviews.setEnabled(True)
        self.ButtonViewWriteReviews.setMinimumSize(QtCore.QSize(140, 0))
        self.ButtonViewWriteReviews.setMaximumSize(QtCore.QSize(140, 40))
        self.ButtonViewWriteReviews.setCheckable(False)
        self.ButtonViewWriteReviews.setAutoDefault(False)
        self.ButtonViewWriteReviews.setDefault(False)
        self.ButtonViewWriteReviews.setFlat(False)
        self.ButtonViewWriteReviews.setObjectName("ButtonViewWriteReviews")
        self.horizontalLayout_3.addWidget(self.ButtonViewWriteReviews)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.gridLayout_3.addWidget(self.frame_3, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.searchByZip = QtWidgets.QRadioButton(self.frame)
        self.searchByZip.setMinimumSize(QtCore.QSize(216, 17))
        self.searchByZip.setObjectName("searchByZip")
        self.gridLayout.addWidget(self.searchByZip, 1, 0, 1, 2)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget_2.sizePolicy().hasHeightForWidth())
        self.stackedWidget_2.setSizePolicy(sizePolicy)
        self.stackedWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.page_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inputCity = QtWidgets.QTextEdit(self.page_3)
        self.inputCity.setMinimumSize(QtCore.QSize(0, 0))
        self.inputCity.setMaximumSize(QtCore.QSize(172, 30))
        self.inputCity.setObjectName("inputCity")
        self.horizontalLayout.addWidget(self.inputCity)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.inputState = QtWidgets.QTextEdit(self.page_3)
        self.inputState.setMinimumSize(QtCore.QSize(0, 0))
        self.inputState.setMaximumSize(QtCore.QSize(172, 30))
        self.inputState.setObjectName("inputState")
        self.horizontalLayout.addWidget(self.inputState)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.inputZip = QtWidgets.QTextEdit(self.page_4)
        self.inputZip.setMinimumSize(QtCore.QSize(0, 0))
        self.inputZip.setMaximumSize(QtCore.QSize(172, 30))
        self.inputZip.setObjectName("inputZip")
        self.horizontalLayout_2.addWidget(self.inputZip)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.stackedWidget_2.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget_2, 3, 0, 1, 2)
        self.valueLimitSearchArea = QtWidgets.QSpinBox(self.frame)
        self.valueLimitSearchArea.setEnabled(True)
        self.valueLimitSearchArea.setMinimumSize(QtCore.QSize(0, 0))
        self.valueLimitSearchArea.setMaximumSize(QtCore.QSize(100, 30))
        self.valueLimitSearchArea.setMaximum(999999999)
        self.valueLimitSearchArea.setObjectName("valueLimitSearchArea")
        self.gridLayout.addWidget(self.valueLimitSearchArea, 2, 1, 1, 1)
        self.limitSearchArea = QtWidgets.QCheckBox(self.frame)
        self.limitSearchArea.setMinimumSize(QtCore.QSize(148, 17))
        self.limitSearchArea.setObjectName("limitSearchArea")
        self.gridLayout.addWidget(self.limitSearchArea, 2, 0, 1, 1)
        self.searchByCityState = QtWidgets.QRadioButton(self.frame)
        self.searchByCityState.setMinimumSize(QtCore.QSize(216, 17))
        self.searchByCityState.setChecked(True)
        self.searchByCityState.setObjectName("searchByCityState")
        self.gridLayout.addWidget(self.searchByCityState, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame.raise_()
        self.MarketTable.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.frame_5 = QtWidgets.QFrame(self.page_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 380, 881, 231))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.page_2)
        self.frame_6.setGeometry(QtCore.QRect(10, 120, 881, 251))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setGeometry(QtCore.QRect(10, 10, 881, 101))
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.selectedMarketName = QtWidgets.QLabel(self.frame_7)
        self.selectedMarketName.setGeometry(QtCore.QRect(10, 10, 861, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.selectedMarketName.setFont(font)
        self.selectedMarketName.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.selectedMarketName.setObjectName("selectedMarketName")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FarmersMarkets"))
        self.ButtonViewAllMarkets.setText(_translate("MainWindow", "Просмотреть все рынки"))
        self.ButtonFindMarkets.setText(_translate("MainWindow", "Найти рынки"))
        self.label.setText(_translate("MainWindow", "Для просмотра или создания\n"
" рецензии введите Fmid рынка"))
        self.inputFmid.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите Fmid</p></body></html>"))
        self.ButtonViewWriteReviews.setText(_translate("MainWindow", "Просмотреть или\n"
" оставить рецензию"))
        self.searchByZip.setText(_translate("MainWindow", "Поиск по почтовому индексу"))
        self.inputCity.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите город</p></body></html>"))
        self.inputState.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите штат</p></body></html>"))
        self.inputZip.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Введите почтовый индекс</p></body></html>"))
        self.limitSearchArea.setText(_translate("MainWindow", "Ограничить зону поиска"))
        self.searchByCityState.setText(_translate("MainWindow", "Поиск по городу и штату"))
        self.selectedMarketName.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
