from PyQt5 import QtCore, QtGui, QtWidgets
from GuppyUI import Ui_MainWindow
import sys
import os.path


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## basecalling
        self.ui.pushButton.clicked.connect(self.select_input_folder)
        self.ui.pushButton_2.clicked.connect(self.select_output_folder)
        self.ui.comboBox.currentIndexChanged.connect(self.select_flowcell)
        self.ui.comboBox_2.currentIndexChanged.connect(self.select_kit)
        self.ui.checkBox.stateChanged.connect(self.onClicked)
        self.ui.pushButton_3.clicked.connect(self.generate_cmd)
        self.input_folder = ""
        self.input_folder_cmd = ""
        self.output_folder = ""
        self.output_folder_cmd = ""
        self.flowcell = ""
        self.flowcell_cmd = ""
        self.kit = ""
        self.kit_cmd = ""
        self.cuda = ""

        ## barcoding

    def select_input_folder(self):
        self.ui.label_7.setText("")
        self.input_folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.textEdit.setText(self.input_folder)
        self.input_folder_cmd = "-i " + self.input_folder

    def select_output_folder(self):
        self.ui.label_8.setText("")
        self.output_folder = QtWidgets.QFileDialog.getExistingDirectory()
        self.ui.textEdit_2.setText(self.output_folder)
        self.output_folder_cmd = "-s " + self.output_folder

    def select_flowcell(self):
        self.flowcell = self.ui.comboBox.currentText()
        self.flowcell_cmd = "--flowcell " + self.flowcell

    def select_kit(self):
        self.kit = self.ui.comboBox_2.currentText()
        self.kit_cmd = "--kit " + self.kit

    def onClicked(self):
        if self.ui.checkBox.isChecked():
            self.cuda = "--device cuda:0"
        else:
            self.cuda = ""

    def generate_cmd(self):
        error = self.check()
        if not error:
            cmd = "guppy_basecaller {} {} {} {} {}"\
                .format(self.input_folder_cmd, self.output_folder_cmd, self.flowcell_cmd, self.kit_cmd, self.cuda)
            self.ui.textEdit_3.setText(cmd)
            self.ui.label_5.setText("")
            self.ui.label_7.setText("")
            self.ui.label_8.setText("")
        else:
            self.ui.label_5.setStyleSheet("color: red; font-size:30px")
            self.ui.label_5.setText(error)

    def check(self):
        self.ui.textEdit_3.setText("")
        error_list = []
        error_message = "Please select "
        if not self.input_folder:
            error_list.append("input folder")
        elif not os.path.isdir(self.ui.textEdit.toPlainText()):
            error_list.append("input folder")
            self.ui.label_7.setStyleSheet("color: red")
            self.ui.label_7.setText("This is not a folder")

        if not self.output_folder:
            error_list.append("save folder")
        elif not os.path.isdir(self.ui.textEdit_2.toPlainText()):
            error_list.append("input folder")
            self.ui.label_8.setStyleSheet("color: red")
            self.ui.label_8.setText("This is not a folder")

        if not self.flowcell:
            error_list.append("flowcell")
        if not self.kit:
            error_list.append("kit")
        if not error_list:
            return
        else:
            return error_message + ' ,'.join(error_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())