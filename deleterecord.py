import sys
from PyQt4 import QtGui, QtCore
import csv
class DeleteRecord(QtGui.QMainWindow):
    def csv_reader(file_obj):
        reader = csv.reader(file_obj)
        for row in reader:
            print(" ".join(row))
    def __init__(self):
        super(DeleteRecord, self).__init__()
        self.initUI()
    def initUI(self):      

        list1 = QtGui.QListWidget(self)
        list1.resize(750, 700)
	# getting row number (index) of the record to be deleted
        rownumbertodelete=2 
        i=0
        strcache=str("")
        with open("data.csv") as f:
              reader = csv.reader(f)
              for row in reader:
                if (i!=rownumbertodelete):
                   strcache = strcache + str(row).replace("['","").replace("']","\n") # PARSING DATA
                i+=1
        f = open('data.csv', 'w')
        f.write(strcache)
        f.close()
        self.statusBar()
        self.setGeometry(300, 50, 750, 700)
        self.setWindowTitle('Delete Record by Index')  
        self.show()
def main():
    app = QtGui.QApplication(sys.argv)
    ex = DeleteRecord()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()