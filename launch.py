from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QDialog, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from sys import argv
from os import getcwd
from os.path import exists
from FolderOrganizer import organize
class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        loadUi("gui.ui", self)
        self.setWindowIcon(QIcon('media\\icon.png'))
        self.setWindowTitle('Folder Organizer')
        self.setFixedSize(415, 140)
        self.path_text.setReadOnly(True)
        self.path_text.setPlaceholderText(f'Please select a folder in order to organize it')
        self.browse.clicked.connect(self.browsefiles)
        self.organize_button.clicked.connect(self.organizefiles)
        self.show()
    def browsefiles(self):
        folder_path = QFileDialog.getExistingDirectory(self, 'Open file',f'{getcwd()}')
        self.path_text.setText(folder_path)
        if self.path_text.displayText() == '':
            self.path_text.setPlaceholderText(f'Please select a valid folder in order to organize it')
            self.organize_button.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid gray;\n"
"    color: rgb(156, 156, 156);\n"
"    background-color: rgb(71, 71, 71);\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"border-radius: 15px;\n"
"}")
        else:
        	self.organize_button.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid #780760;\n"
"    color: #e6b1db;\n"
"    background-color: rgb(71, 71, 71);\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"border-radius: 15px;\n"
"}")
    def organizefiles(self):
        directory = self.path_text.displayText()
        if directory != '':
            if exists(directory):
                try:
                    success = organize(directory)
                    if success:
                        self.successPopOut()

                    else:
                    	self.failurePopOut()
                    self.organize_button.setStyleSheet("QPushButton {\n"
"    border: 0.5px solid gray;\n"
"    color: rgb(156, 156, 156);\n"
"    background-color: rgb(71, 71, 71);\n"
"  text-align: center;\n"
"  text-decoration: none;\n"
"border-radius: 15px;\n"
"}")
                except Exception as error:
                    print(error)
            else:
                print("The directory path you want to organize doesn't exists")
    def successPopOut(self):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon('media\\icon.png'))
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Success!")
        msg.setText("The folder was succesfuly organized!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    def failurePopOut(self):
        msg = QMessageBox()
        msg.setWindowIcon(QIcon('media\\icon.png'))
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Failure!")
        msg.setText("The files are already organized!")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

app = QApplication(argv)
window = UI()
app.exec_()