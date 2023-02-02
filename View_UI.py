import Script_UI
import ETL
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FarmerMarkets(Script_UI.Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
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



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_FarmerMarkets()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

