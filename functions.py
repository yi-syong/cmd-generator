from PyQt5 import QtCore, QtGui, QtWidgets
from MainUI import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.select_input_folder)
        self.ui.pushButton_2.clicked.connect(self.select_output_folder)
        self.ui.comboBox.currentIndexChanged.connect(self.select_flowcell)
        self.ui.comboBox_2.currentIndexChanged.connect(self.select_kit)
        self.ui.radioButton.toggled.connect(self.onClicked)
        self.ui.radioButton_2.toggled.connect(self.onClicked)
        self.ui.pushButton_3.clicked.connect(self.generate_cmd)
        self.input_folder = ""
        self.output_folder = ""
        self.flowcell = ""
        self.kit = ""
        self.cuda = ""

    def select_input_folder(self):
        input_folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.textEdit.setText(input_folder)
        self.input_folder = "-i " + input_folder
        print(self.input_folder)

    def select_output_folder(self):
        output_folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.textEdit_2.setText(output_folder)
        self.output_folder = "-s " + output_folder

    def select_flowcell(self):
        flowcell = self.ui.comboBox.currentText()
        self.flowcell = "--flowcell " + flowcell

    def select_kit(self):
        kit = self.ui.comboBox_2.currentText()
        self.kit = "--kit " + kit

    def onClicked(self):
        if self.ui.radioButton.isChecked():
            self.cuda = ""
        else:
            self.cuda = "--device cuda:0"

    def generate_cmd(self):
        cmd = "guppy_basecaller {} {} {} {} {}"\
            .format(self.input_folder, self.output_folder, self.flowcell, self.kit, self.cuda)
        self.ui.textEdit_3.setText(cmd)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())