# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InfoProject(object):
    def setupUi(self, InfoProject):
        InfoProject.setObjectName("InfoProject")
        InfoProject.resize(607, 668)
        self.centralwidget = QtWidgets.QWidget(InfoProject)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 581, 51))
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.inputText = QtWidgets.QTextEdit(self.frame)
        self.inputText.setGeometry(QtCore.QRect(170, 10, 391, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inputText.sizePolicy().hasHeightForWidth())
        self.inputText.setSizePolicy(sizePolicy)
        self.inputText.setObjectName("inputText")
        self.inputLabel = QtWidgets.QLabel(self.frame)
        self.inputLabel.setGeometry(QtCore.QRect(10, 10, 151, 30))
        self.inputLabel.setObjectName("inputLabel")
        self.functions = QtWidgets.QGroupBox(self.centralwidget)
        self.functions.setGeometry(QtCore.QRect(20, 70, 551, 121))
        self.functions.setObjectName("functions")
        self.nmap = QtWidgets.QPushButton(self.functions)
        self.nmap.setGeometry(QtCore.QRect(10, 30, 93, 30))
        self.nmap.setObjectName("nmap")
        self.ftp = QtWidgets.QPushButton(self.functions)
        self.ftp.setGeometry(QtCore.QRect(110, 30, 161, 30))
        self.ftp.setObjectName("ftp")
        self.dlink = QtWidgets.QPushButton(self.functions)
        self.dlink.setGeometry(QtCore.QRect(280, 30, 171, 30))
        self.dlink.setObjectName("dlink")
        self.d9 = QtWidgets.QPushButton(self.functions)
        self.d9.setGeometry(QtCore.QRect(460, 30, 81, 30))
        self.d9.setObjectName("d9")
        self.whois = QtWidgets.QPushButton(self.functions)
        self.whois.setGeometry(QtCore.QRect(10, 70, 93, 28))
        self.whois.setObjectName("whois")
        self.label = QtWidgets.QLabel(self.functions)
        self.label.setGeometry(QtCore.QRect(110, 80, 211, 16))
        self.label.setObjectName("label")
        self.Output = QtWidgets.QGroupBox(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 200, 551, 351))
        self.Output.setObjectName("Output")
        self.outputText = QtWidgets.QLabel(self.Output)
        self.outputText.setGeometry(QtCore.QRect(20, 30, 521, 311))
        font = QtGui.QFont()
        font.setFamily("Microsoft PhagsPa")
        font.setPointSize(8)
        self.outputText.setFont(font)
        self.outputText.setAutoFillBackground(False)
        self.outputText.setText("")
        self.outputText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.outputText.setWordWrap(True)
        self.outputText.setObjectName("outputText")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(20, 560, 111, 28))
        self.save.setObjectName("save")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(460, 560, 111, 28))
        self.clear.setObjectName("clear")
        InfoProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InfoProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        InfoProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InfoProject)
        self.statusbar.setObjectName("statusbar")
        InfoProject.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(InfoProject)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(InfoProject)
        QtCore.QMetaObject.connectSlotsByName(InfoProject)

    def retranslateUi(self, InfoProject):
        _translate = QtCore.QCoreApplication.translate
        InfoProject.setWindowTitle(_translate("InfoProject", "MainWindow"))
        self.inputText.setHtml(_translate("InfoProject", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.inputLabel.setText(_translate("InfoProject", "Enter Domain/IP Address::"))
        self.functions.setTitle(_translate("InfoProject", "Available Functions"))
        self.nmap.setText(_translate("InfoProject", "Nmap Scan"))
        self.ftp.setText(_translate("InfoProject", "FTP Backdoor Detection"))
        self.dlink.setText(_translate("InfoProject", "Http-dlink Backdoor Scan"))
        self.d9.setText(_translate("InfoProject", "d9 Scan"))
        self.whois.setText(_translate("InfoProject", "Whois"))
        self.label.setText(_translate("InfoProject", "(Require domain name to execute)"))
        self.Output.setTitle(_translate("InfoProject", "Output"))
        self.save.setText(_translate("InfoProject", "Save to text file"))
        self.clear.setText(_translate("InfoProject", "Clear"))
        self.menuFile.setTitle(_translate("InfoProject", "File"))
        self.actionExit.setText(_translate("InfoProject", "Exit"))