import sys
from PyQt4 import QtGui, QtCore
import csv

class NewRecord(QtGui.QMainWindow):
        def __init__(self):
        super(NewRecord, self).__init__()
        self.initUI()
    def initUI(self):
        # defining new textboxes
        name_newtextbox = QtGui.QLineEdit(self)
        surname_newtextbox = QtGui.QLineEdit(self)
        tel_newtextbox = QtGui.QLineEdit(self)
        address_newtextbox = QtGui.QLineEdit(self) 
        ID_newtextbox = QtGui.QLineEdit(self) 
         # defining new titles for textboxes
        name_newlabel = QtGui.QLabel("Ad:",self)
        surname_newlabel = QtGui.QLabel("Soyad:",self)
        tel_newlabel = QtGui.QLabel("Tel:",self)
        address_newlabel = QtGui.QLabel("Adres:",self)
        ID_newlabel = QtGui.QLabel("ID:",self)
         # defining textbox coordinates
        name_newtextbox.move(50, 50)
        surname_newtextbox.move(50, 100)
        tel_newtextbox.move(50,150)
        address_newtextbox.move(50, 200)
        ID_newtextbox.move(50, 250)
          # defining label coordinates
        name_newlabel.move(10, 50)
        surname_newlabel.move(10, 100)
        tel_newlabel.move(10,150)
        address_newlabel.move(10, 200)
        ID_newlabel.move(10, 250)
          # 'add new record' button
        btn2 = QtGui.QPushButton("Add Record", self)
        btn2.move(30, 350)
      
        btn2.clicked.connect(self.buttonClicked)
        self.statusBar()
        self.setGeometry(300, 50, 250, 400)
        self.setWindowTitle('New Record Page')   # adding window title
        self.show()
        
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage("Record has been added.")   # showing confirmation message
        fd = open('data.csv','a')   # appending new data line into csv via pandas
        fd.write(self.name_newtextbox.Text() + ";" + self.surname_newtextbox.Text() + ";" + self.tel_newtextbox.Text()  + ";" + self.address_newtextbox.Text()  + ";" + self.ID_newtextbox.Text()   + "\n")
        fd.close()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = NewRecord()
    sys.exit(app.exec_())
if __name__ == '__main__':
main()