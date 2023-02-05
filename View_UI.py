import Script_UI
import ETL
import model
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FarmerMarkets(Script_UI.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.add_function()
        self.search_function()
        self.changeSearchPage()
        self.hideValueLimitSearchArea()
        self.changeLimitSearchArea()
        self.chekChangeFmid()
        self.setEnabledButtonViewWriteReviews()
        self.clickedButtonButtonViewWriteReviews()
        self.stackedWidget.setCurrentIndex(0)

    def changeSearchPage(self):
        # self.searchByCityState.isChecked.(lambda: self.SetCurrentIndex())
        self.searchByCityState.toggled.connect(lambda: self.SetCurrentIndexSearchPage())
        self.searchByZip.toggled.connect(lambda: self.SetCurrentIndexSearchPage())

    def SetCurrentIndexSearchPage(self):
        if self.searchByCityState.isChecked():
            self.stackedWidget_2.setCurrentIndex(0)
        elif self.searchByZip.isChecked():
            self.stackedWidget_2.setCurrentIndex(1)

    def add_function(self):
        self.ButtonViewAllMarkets.clicked.connect(lambda: self.ShowAllMarkets())

    def ShowAllMarkets(self):
        fermMarketsList = ETL.getAllMarkets()
        self.ShowMarkets(fermMarketsList)

    def ShowMarkets(self, fermMarketList):
        if fermMarketList != []:
            self.MarketTable.setRowCount(len(fermMarketList))
            self.MarketTable.setColumnCount(len(fermMarketList[0].columnNameMain))
            self.MarketTable.setHorizontalHeaderLabels(fermMarketList[0].columnNameMain)

            for i in range(len(fermMarketList)):
                for j in range(len(fermMarketList[0].columnNameMain)):
                    if j == 0:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(fermMarketList[i].FMID)))
                    elif j == 1:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(fermMarketList[i].MarketName))
                    elif j == 2:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(fermMarketList[i].city))
                    elif j == 3:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(fermMarketList[i].County))
                    elif j == 4:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(fermMarketList[i].State))
                    elif j == 5:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(str(fermMarketList[i].zip)))
                    elif j == 6:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(f"{fermMarketList[i].x:.1f}"))
                    elif j == 7:
                        self.MarketTable.setItem(i, j, QtWidgets.QTableWidgetItem(f"{fermMarketList[i].y:.1f}"))
            self.MarketTable.resizeColumnsToContents()
        else:
            self.MarketTable.clear()


    def search_function(self):
        self.ButtonFindMarkets.clicked.connect(lambda: self.searchMarkets())

    def searchMarkets(self):
        fermMarketList = ETL.getAllMarkets()

        if self.limitSearchArea.isChecked():
            x = -89.5
            y = 34.4
            r = self.valueLimitSearchArea.value()
            fermMarketList = model.srchByArea(fermMarketList, x, y, r)

        if self.searchByCityState.isChecked():
            city = self.inputCity.toPlainText()
            state = self.inputState.toPlainText()
            search_list = model.srchBycityandstate(fermMarketList, city, state)
            self.ShowMarkets(search_list)
        elif self.searchByZip.isChecked():
            zip = self.inputZip.toPlainText()
            search_list = model.srchByZip(fermMarketList, zip)
            self.ShowMarkets(search_list)

    def changeLimitSearchArea(self):
        self.limitSearchArea.toggled.connect(lambda: self.hideValueLimitSearchArea())

    def hideValueLimitSearchArea(self):
        if self.limitSearchArea.isChecked():
            self.valueLimitSearchArea.show()
        else:
            self.valueLimitSearchArea.hide()

    def chekChangeFmid(self):
        self.inputFmid.textChanged.connect(lambda: self.setEnabledButtonViewWriteReviews())


    def setEnabledButtonViewWriteReviews(self):
        try:
            fmid = int(self.inputFmid.toPlainText())
        except ValueError:
            self.ButtonViewWriteReviews.setEnabled(False)
        else:
            fermMarketList = ETL.getAllMarkets()
            if model.chekOccurFmid(fermMarketList, fmid):
                self.ButtonViewWriteReviews.setEnabled(True)
                self.selectedFmid = fmid
            else:
                self.ButtonViewWriteReviews.setEnabled(False)

    def clickedButtonButtonViewWriteReviews(self):
        self.ButtonViewWriteReviews.clicked.connect(lambda: self.openReviewPage())

    def openReviewPage(self):
        self.stackedWidget.setCurrentIndex(1)
        print(self.selectedFmid)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FarmerMarkets()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

