# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yi-syong/Desktop/analysis_UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_3.setGeometry(QtCore.QRect(100, 510, 731, 61))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 460, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(100, 280, 261, 161))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 71, 31))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(100, 30, 121, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(100, 100, 121, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(0, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(400, 280, 161, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(40, 30, 81, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(40, 90, 81, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(30, 140, 101, 16))
        self.label_6.setObjectName("label_6")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(100, 50, 731, 191))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 31))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit.setGeometry(QtCore.QRect(130, 40, 481, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(630, 40, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 81, 31))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_3)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 120, 481, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(630, 120, 31, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(100, 590, 731, 91))
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 962, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "generate cmd"))
        self.label_4.setText(_translate("MainWindow", "Kit"))
        self.label_3.setText(_translate("MainWindow", "flowcell"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FLO-PRO001"))
        self.comboBox.setItemText(2, _translate("MainWindow", "FLO-PRO002"))
        self.comboBox.setItemText(3, _translate("MainWindow", "FLO-FLG001"))
        self.comboBox.setItemText(4, _translate("MainWindow", "FLO-MIN106"))
        self.comboBox.setItemText(5, _translate("MainWindow", "FLO-MIN107"))
        self.comboBox.setItemText(6, _translate("MainWindow", "FLO-MIN110"))
        self.comboBox.setItemText(7, _translate("MainWindow", "FLO-MIN111"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "SQK-LSK109"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SQK-LSK109-XL"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "SQK-DCS109"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "SQK-PCS109"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "SQK-PRC109"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "SQK-PCB109"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "SQK-LSK110"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "SQK-CAS109"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "SQK-CS9109"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "SQK-DCS108"))
        self.comboBox_2.setItemText(11, _translate("MainWindow", "SQK-LRK001"))
        self.comboBox_2.setItemText(12, _translate("MainWindow", "SQK-LSK108"))
        self.comboBox_2.setItemText(13, _translate("MainWindow", "SQK-LWP001"))
        self.comboBox_2.setItemText(14, _translate("MainWindow", "SQK-PCS108"))
        self.comboBox_2.setItemText(15, _translate("MainWindow", "SQK-PSK004"))
        self.comboBox_2.setItemText(16, _translate("MainWindow", "SQK-RAD002"))
        self.comboBox_2.setItemText(17, _translate("MainWindow", "SQK-RAD003"))
        self.comboBox_2.setItemText(18, _translate("MainWindow", "SQK-RAD004"))
        self.comboBox_2.setItemText(19, _translate("MainWindow", "SQK-RAS201"))
        self.comboBox_2.setItemText(20, _translate("MainWindow", "SQK-RLI001"))
        self.comboBox_2.setItemText(21, _translate("MainWindow", "VSK-VBK001"))
        self.comboBox_2.setItemText(22, _translate("MainWindow", "VSK-VSK001"))
        self.comboBox_2.setItemText(23, _translate("MainWindow", "VSK-VSK002"))
        self.comboBox_2.setItemText(24, _translate("MainWindow", "SQK-16S024"))
        self.comboBox_2.setItemText(25, _translate("MainWindow", "SQK-RBK001"))
        self.comboBox_2.setItemText(26, _translate("MainWindow", "SQK-RBK004"))
        self.comboBox_2.setItemText(27, _translate("MainWindow", "SQK-RLB001"))
        self.comboBox_2.setItemText(28, _translate("MainWindow", "SQK-LWB001"))
        self.comboBox_2.setItemText(29, _translate("MainWindow", "SQK-PBK004"))
        self.comboBox_2.setItemText(30, _translate("MainWindow", "SQK-RAB201"))
        self.comboBox_2.setItemText(31, _translate("MainWindow", "SQK-RAB204"))
        self.comboBox_2.setItemText(32, _translate("MainWindow", "SQK-RPB004"))
        self.comboBox_2.setItemText(33, _translate("MainWindow", "VSK-VMK001"))
        self.comboBox_2.setItemText(34, _translate("MainWindow", "VSK-VMK002"))
        self.comboBox_2.setItemText(35, _translate("MainWindow", "SQK-RNA002"))
        self.comboBox_2.setItemText(36, _translate("MainWindow", "SQK-LSK308"))
        self.comboBox_2.setItemText(37, _translate("MainWindow", "SQK-LSK309"))
        self.comboBox_2.setItemText(38, _translate("MainWindow", "SQK-LSK319"))
        self.comboBox_2.setItemText(39, _translate("MainWindow", "SQK-RNA001"))
        self.comboBox_2.setItemText(40, _translate("MainWindow", "SQK-RNA002"))
        self.radioButton.setText(_translate("MainWindow", "CPU"))
        self.radioButton_2.setText(_translate("MainWindow", "GPU"))
        self.label_6.setText(_translate("MainWindow", "(Default: CPU)"))
        self.label.setText(_translate("MainWindow", "Input folder"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Save folder"))
        self.pushButton_2.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Basecalling"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Barcoder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
