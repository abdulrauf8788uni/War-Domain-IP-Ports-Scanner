from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import sys
import subprocess
import whois11
import os

class Ui_InfoProject(object):            
    def iprint(self, text, end='\n'):
        self.outputText.setText(f"{self.outputText.text()}{end}{text}")

    def clear_console(self):
        self.outputText.clear()

    def save_txt(self):
        # Error Handling
        exists = os.path.exists('saves/output1.txt')
        if not exists:
            try:
                os.mkdir("saves")
            except: 
                pass
            new_num = 1
        else:
            max_num = 0
            dirnames = os.listdir('saves')
            filenumbers = list(map(lambda x: int(x[6:-4]), dirnames))
            new_num = max(filenumbers) + 1

        with open(f"saves/output{new_num}.txt", "w") as f:
            f.write(self.outputText.text()) 




    def scan(self, choice):
        target = self.inputText.toPlainText()
        # Check for valid IP Address
        if target == "":
            self.iprint("Invalid format. Please use a correct IP or web address")
            return
        # Set socket timeout
        socket.setdefaulttimeout(0.90)
        # Check for valid ip address
        try:
            t_ip = socket.gethostbyname(target)
        except (UnboundLocalError, socket.gaierror):
            self.iprint("Invalid format. Please use a correct IP or web address")
            return
        # Clear Output
        self.outputText.clear()

        # Initailize conmmands
        nmapScan = "nmap -v -A {}".format(target)
        backdoor = "nmap -sV --script http-dlink-backdoor {ip}".format(ip=target) 
        ftpbackdoor = "nmap --script ftp-proftpd-backdoor -p 21 {ip}".format(ip=target)
        ping = "nmap -sn {ip}".format(ip=target)
        topports = "nmap -top-ports 10 {ip}".format(ip=target)
        exportfile = "nmap -oN output.txt {ip}".format(ip=target)
        detectservices = "nmap -sV {ip}".format(ip=target)
        CVEdetection = "nmap -Pn –script vuln {ip}".format(ip=target)

        # Conditions
        # if choice =="1":
        #     os.system(ping)
        # elif choice == "2":
        #     os.system(nmapScan)
        # elif choice == "3":
        #     os.system(ftpbackdoor)
        # elif choice == "4":
        #     os.system(backdoor)
        # elif choice == "5":
        #     os.system(CVEdetection)
        # elif choice == "6":
        #     os.system(detectservices)
        # elif choice == "7":
        #     os.system(topports)
        # elif choice == "8":
        #     whois11.whois(str(target))
        # else:
        #     pass

        if choice =="1":
            output = subprocess.check_output(ping.strip())
        elif choice == "2":
            output = subprocess.check_output(nmapScan.strip())
        elif choice == "3":
            output = subprocess.check_output(ftpbackdoor.strip())
        elif choice == "4":
            output = subprocess.check_output(backdoor.strip())
        elif choice == "5":
            output = subprocess.check_output(CVEdetection.strip())
        elif choice == "6":
            output = subprocess.check_output(detectservices.strip())
        elif choice == "7":
            output = subprocess.check_output(topports.strip())
        elif choice == "8":
            try:
                chrs = whois11.whois(str(target))
                for i in range(len(chrs)):
                     if chrs[i]=='>' and chrs[i+1]=='>' and chrs[i+2]=='>':
                         return
                     self.iprint(chrs[i], end='')
            except:
                self.iprint("Error during execution.")
                return 
        else:
            pass

        self.iprint(output.decode())



    def setupUi(self, InfoProject):
        InfoProject.setObjectName("InfoProject")
        InfoProject.resize(607, 636)
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
        self.ping = QtWidgets.QPushButton(self.functions)
        self.ping.setGeometry(QtCore.QRect(10, 30, 93, 30))
        self.ping.setObjectName("ping")
        self.ping.clicked.connect(lambda: self.scan("1"))
        self.nmap = QtWidgets.QPushButton(self.functions)
        self.nmap.setGeometry(QtCore.QRect(110, 30, 93, 30))
        self.nmap.setObjectName("nmap")
        self.nmap.clicked.connect(lambda: self.scan("2"))     
        self.ftp = QtWidgets.QPushButton(self.functions)
        self.ftp.setGeometry(QtCore.QRect(10, 70, 161, 30))
        self.ftp.setObjectName("ftp")
        self.ftp.clicked.connect(lambda: self.scan("3"))
        self.dlink = QtWidgets.QPushButton(self.functions)
        self.dlink.setGeometry(QtCore.QRect(340, 70, 201, 30))
        self.dlink.setObjectName("dlink")
        self.dlink.clicked.connect(lambda: self.scan("4"))
        self.cve = QtWidgets.QPushButton(self.functions)
        self.cve.setGeometry(QtCore.QRect(300, 30, 101, 30))
        self.cve.setObjectName("cve")
        self.cve.clicked.connect(lambda: self.scan("5"))
        self.services = QtWidgets.QPushButton(self.functions)
        self.services.setGeometry(QtCore.QRect(410, 30, 131, 30))
        self.services.setObjectName("services")
        self.services.clicked.connect(lambda: self.scan("6"))
        self.ports = QtWidgets.QPushButton(self.functions)
        self.ports.setGeometry(QtCore.QRect(180, 70, 151, 30))
        self.ports.setObjectName("ports")
        self.ports.clicked.connect(lambda: self.scan("7"))
        self.whois = QtWidgets.QPushButton(self.functions)
        self.whois.setGeometry(QtCore.QRect(210, 30, 81, 30))
        self.whois.setObjectName("whois")
        self.whois.clicked.connect(lambda: self.scan("8"))
        self.Output = QtWidgets.QGroupBox(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(20, 200, 551, 321))
        self.Output.setObjectName("Output")
        self.outputText = QtWidgets.QLabel(self.Output)
        self.outputText.setGeometry(QtCore.QRect(10, 20, 531, 291))
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
        self.save.setGeometry(QtCore.QRect(20, 530, 111, 28))
        self.save.setObjectName("save")
        self.save.clicked.connect(lambda: self.save_txt())
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(460, 530, 111, 28))
        self.clear.setObjectName("clear")
        self.clear.clicked.connect(lambda: self.clear_console())
        InfoProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(InfoProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 26))
        self.menubar.setObjectName("menubar")
        InfoProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(InfoProject)
        self.statusbar.setObjectName("statusbar")
        InfoProject.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(InfoProject)
        self.actionExit.setObjectName("actionExit")

        self.retranslateUi(InfoProject)
        QtCore.QMetaObject.connectSlotsByName(InfoProject)




    def retranslateUi(self, InfoProject):
        _translate = QtCore.QCoreApplication.translate
        InfoProject.setWindowTitle(_translate("InfoProject", "Info Project"))
        self.inputText.setHtml(_translate("InfoProject", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.inputLabel.setText(_translate("InfoProject", "Enter Domain/IP Address::"))
        self.functions.setTitle(_translate("InfoProject", "Available Functions"))
        self.ping.setText(_translate("InfoProject", "Ping"))
        self.nmap.setText(_translate("InfoProject", "Nmap Scan"))
        self.ftp.setText(_translate("InfoProject", "FTP Backdoor Detection"))
        self.dlink.setText(_translate("InfoProject", "HTTP-DLink Backdoor Detection"))
        self.cve.setText(_translate("InfoProject", "CVE Detection"))
        self.services.setText(_translate("InfoProject", "Services Detection"))
        self.ports.setText(_translate("InfoProject", "Scan Vulnerable Ports"))
        self.whois.setText(_translate("InfoProject", "WhoIs"))
        self.Output.setTitle(_translate("InfoProject", "Output"))
        self.save.setText(_translate("InfoProject", "Save to text file"))
        self.clear.setText(_translate("InfoProject", "Clear"))
        self.actionExit.setText(_translate("InfoProject", "Exit"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    InfoProject = QtWidgets.QMainWindow()
    ui = Ui_InfoProject()
    ui.setupUi(InfoProject)
    InfoProject.show()
    sys.exit(app.exec_())
