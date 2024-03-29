import ETL
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
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
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.stackedWidget_2.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget_2, 3, 0, 1, 2)
        self.valueLimitSearchArea = QtWidgets.QSpinBox(self.frame)
        self.valueLimitSearchArea.setMinimumSize(QtCore.QSize(0, 0))
        self.valueLimitSearchArea.setMaximumSize(QtCore.QSize(100, 30))
        self.valueLimitSearchArea.setObjectName("valueLimitSearchArea")
        self.gridLayout.addWidget(self.valueLimitSearchArea, 2, 1, 1, 1)
        self.limitSearchArea = QtWidgets.QCheckBox(self.frame)
        self.limitSearchArea.setMinimumSize(QtCore.QSize(148, 17))
        self.limitSearchArea.setObjectName("limitSearchArea")
        self.gridLayout.addWidget(self.limitSearchArea, 2, 0, 1, 1)
        self.searchByCityState = QtWidgets.QRadioButton(self.frame)
        self.searchByCityState.setMinimumSize(QtCore.QSize(216, 17))
        self.searchByCityState.setObjectName("searchByCityState")
        self.gridLayout.addWidget(self.searchByCityState, 0, 0, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setMinimumSize(QtCore.QSize(150, 0))
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
        self.gridLayout_3.addWidget(self.frame_2, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 0, 1, 1, 1)
        self.MarketTable = QtWidgets.QTableWidget(self.page)
        self.MarketTable.setMinimumSize(QtCore.QSize(0, 0))
        self.MarketTable.setObjectName("MarketTable")
        self.MarketTable.setColumnCount(0)
        self.MarketTable.setRowCount(0)
        self.gridLayout_3.addWidget(self.MarketTable, 1, 0, 1, 3)
        self.frame.raise_()
        self.MarketTable.raise_()
        self.frame_2.raise_()
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.add_function()


    def add_function(self):
        self.ButtonViewAllMarkets.clicked.connect(lambda: self.ShowAllMarkets())

    def ShowAllMarkets(self):
        fermMarketList = ETL.getAllMarkets()
        self.MarketTable.setRowCount(len(fermMarketList))
        self.MarketTable.setColumnCount(len(fermMarketList[0].columnNameMain))
        self.MarketTable.setHorizontalHeaderLabels(fermMarketList[0].columnNameMain)

        for i in range(len(fermMarketList)):
            for j in range(len(fermMarketList[0].columnNameMain)):
                if j == 0:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(str(fermMarketList[i].FMID)))
                elif j == 1:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(fermMarketList[i].MarketName))
                elif j == 2:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(fermMarketList[i].city))
                elif j == 3:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(fermMarketList[i].County))
                elif j == 4:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(fermMarketList[i].State))
                elif j == 5:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(str(fermMarketList[i].zip)))
                elif j == 6:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(f"{fermMarketList[i].x:.1f}"))
                elif j == 7:
                    self.MarketTable.setItem(i,j, QtWidgets.QTableWidgetItem(f"{fermMarketList[i].y:.1f}"))  

        self.MarketTable.resizeColumnsToContents()

          

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
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
        self.ButtonViewAllMarkets.setText(_translate("MainWindow", "Просмотреть все рынки"))
        self.ButtonFindMarkets.setText(_translate("MainWindow", "Найти рынки"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())