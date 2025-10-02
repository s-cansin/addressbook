import sys
from PyQt4 import QtGui, QtCore
import csv
from pyfpdf import FPDF
import tkFileDialog
class ConvertToPDF(QtGui.QMainWindow):
    def csv_reader(file_obj):
        reader = csv.reader(file_obj)
        for row in reader:
            print(" ".join(row))
        
    def __init__(self):
        super(ConvertToPDF, self).__init__()
        self.initUI()
    def initUI(self):      
        list1 = QtGui.QListWidget(self)
        list1.resize(750, 700)
        rownumbertodelete=0
        i=0
        strcache=str("")
        with open("data.csv") as f:
              reader = csv.reader(f)
              for row in reader:
                   strcache = strcache + str(row).replace("['","").replace("']","\n")
       
                
	#CONVERTING TO PDF FILE
        file_path_string = tkFileDialog.asksaveasfile(mode='w', defaultextension=".pdf")
        pdf = FPDF() # we export data with using pyfpdf library
        pdf.add_page()
        pdf.set_font('Courier','B',16)
        pdf.cell(40,10,strcache)
        pdf.output(file_path_string ,'F')

              
        self.statusBar()
        
        self.setGeometry(300, 50, 750, 700)
        self.setWindowTitle('Delete Record by Index')  
        self.show()
                
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ConvertToPDF()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()