import sys
from PyQt4 import QtGui, QtCore
import csv
class MainProgram(QtGui.QMainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.initUI()

   def initUI(self):      
        # creating new buttons and adding
        btn1 = QtGui.QPushButton("New record", self)
        btn1.move(30, 0)             
        btn1.clicked.connect(self.AddMainProgram)
        btn2 = QtGui.QPushButton("List Records", self)
        btn2.move(30, 50)             
        btn2.clicked.connect(self.ListRecords)
        btn3 = QtGui.QPushButton("Delete Record", self)
        btn3.move(30, 100)             
        btn3.clicked.connect(self.DeleteRecord)
        btn4 = QtGui.QPushButton("CSV> PDF", self)
        btn4.move(30, 150)             
        btn4.clicked.connect(self.DeleteRecord)
        self.statusBar()
        self.setGeometry(300, 50, 250, 400)
        self.setWindowTitle('Address Book Main Page')   # Adding window title
        self.show()
        
    def AddMainProgram(self):
        execfile('addnewrecord.py')
    def ListRecords(self):
        execfile('showrecords.py')
    def DeleteRecord(self):
        execfile('deleterecord.py')
    def pdfcikart(self):
        execfile('export.py')
def main():
    app = QtGui.QApplication(sys.argv)
    ex = MainProgram()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()