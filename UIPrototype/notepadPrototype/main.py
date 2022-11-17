from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
import sys
from mainwindow import Ui_MainWindow #Import the compiled python file of the UI


class NotepadWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) #Sets up the UI fro us using the Python file imported above
        self.show()
        
        self.actionSave.triggered.connect(self.save_file)
        
        
    def save_file(self): #The save file button
        filename = QFileDialog.getSaveFileName(self, "Save File")
        
        if filename[0]:
            f = open(filename[0], 'w')
            
            with f:
                text = self.textEdit.toPlainText()
                
                f.write(text)
                
                QMessageBox.about(self, "Save File", "File has been saved")
                
                
        
app = QApplication(sys.argv)
Note = NotepadWindow()
sys.exit(app.exec())