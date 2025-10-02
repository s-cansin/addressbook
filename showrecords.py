import sys
from PyQt4 import QtGui, QtCore
import csv
class ListAddress(QtGui.QMainWindow):
    def __init__(self):
        super(ListAddress, self).__init__()
        self.initUI()
    def initUI(self):
        list1 = QtGui.QListWidget(self) # Creating listbox-like form element where we bind data
        list1.resize(750, 700)
        # Extracting data from CSV file
        with open("data.csv") as f:
              reader = csv.reader(f)
              for row in reader:
                list1.addItem(str(row).replace(";"," - ").replace("['","").replace("']",""))  # Clearing unnecessary characters from data we extract from CSV file
        self.statusBar()
        self.setGeometry(300, 50, 750, 700) # Creating large size form
        self.setWindowTitle('List Address Records')  
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = ListAddress()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()