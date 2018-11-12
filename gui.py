# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test01.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1530, 1051)
        MainWindow.setStyleSheet("QMainWindow{\n"
                                 "    Background-color: rgb(66, 61, 57);\n"
                                 "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QgroupBox{\n"
                                 "border: 0px;\n"
                                 "}")
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setHorizontalSpacing(7)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setMaximumSize(QtCore.QSize(74, 74))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(66, 61, 57);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgba(161, 149, 140, 0);\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color: rgb(66, 61, 57);\n"
                                        "    padding: 10px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "border-style: ridge;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    style: inset;\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                        "stop:0 rgba(84, 77, 73, 255), stop:0.45 rgba(84, 77, 73, 0), stop:0.55 rgba("
                                        "84, 77, 73, 0), stop:1 rgba(84, 77, 73, 255));\n "
                                        "border-style: groove;\n"
                                        "    }")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../HTG/Configurazione/icns/512x512/file-txt.png"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(54, 54))
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_3.addWidget(self.pushButton_4, 0, 6, 2, 1, QtCore.Qt.AlignLeft)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMaximumSize(QtCore.QSize(74, 74))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(66, 61, 57);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgba(161, 149, 140, 0);\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color: rgb(66, 61, 57);\n"
                                        "    padding: 10px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "border-style: ridge;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    style: inset;\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                        "stop:0 rgba(84, 77, 73, 255), stop:0.45 rgba(84, 77, 73, 0), stop:0.55 rgba("
                                        "84, 77, 73, 0), stop:1 rgba(84, 77, 73, 255));\n "
                                        "border-style: groove;\n"
                                        "    }")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../HTG/Configurazione/icns/512x512/file-dxf.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(54, 54))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMaximumSize(QtCore.QSize(74, 74))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(66, 61, 57);\n"
                                        "    border: 2px solid;\n"
                                        "    border-color: rgba(161, 149, 140, 0);\n"
                                        "    border-radius: 20px;\n"
                                        "    background-color: rgb(66, 61, 57);\n"
                                        "    padding: 10px;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:hover {\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "border-style: ridge;\n"
                                        "    }\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    style: inset;\n"
                                        "    border: 2px solid ;\n"
                                        "    border-color: rgb(120, 105, 100);\n"
                                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                        "stop:0 rgba(84, 77, 73, 255), stop:0.45 rgba(84, 77, 73, 0), stop:0.55 rgba("
                                        "84, 77, 73, 0), stop:1 rgba(84, 77, 73, 255));\n "
                                        "border-style: groove;\n"
                                        "    }")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../HTG/Configurazione/icns/512x512/file-csv.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(54, 54))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 0, 3, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(74, 74))
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    color: rgb(66, 61, 57);\n"
                                      "    border: 2px solid;\n"
                                      "    border-color: rgba(161, 149, 140, 0);\n"
                                      "    border-radius: 20px;\n"
                                      "    background-color: rgb(66, 61, 57);\n"
                                      "    padding: 10px;\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    border: 2px solid ;\n"
                                      "    border-color: rgb(120, 105, 100);\n"
                                      "border-style: ridge;\n"
                                      "    }\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    style: inset;\n"
                                      "    border: 2px solid ;\n"
                                      "    border-color: rgb(120, 105, 100);\n"
                                      "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, "
                                      "stop:0 rgba(84, 77, 73, 255), stop:0.45 rgba(84, 77, 73, 0), stop:0.55 rgba("
                                      "84, 77, 73, 0), stop:1 rgba(84, 77, 73, 255));\n "
                                      "border-style: groove;\n"
                                      "    }")
        self.pushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../HTG/Configurazione/icns/512x512/file-opn.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.pushButton.setIconSize(QtCore.QSize(54, 54))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 2)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)

        self.textBrowser.setText(pippoo)

        self.scrollArea = QtWidgets.QScrollArea(self.widget)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1049, 893))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 7)
        self.gridLayout_2.addWidget(self.widget, 1, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1530, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Hole Table Generator ALPHA RELEASE 3.0"))
        self.pushButton_4.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p>Esporta elenchi di coordinate in formato <span "
                                                "style=\" font-size:9pt; "
                                                "font-weight:600;\">TXT</span></p></body></html>"))
        self.pushButton_2.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p>Esporta un disegno dei fori in <span style=\" "
                                                "font-size:9pt; font-weight:600;\">DXF</span></p></body></html>"))
        self.pushButton_3.setToolTip(_translate("MainWindow",
                                                "<html><head/><body><p>Esporta una tabella in formato <span style=\" "
                                                "font-size:9pt; font-weight:600;\">CSV</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "Apri un file VDA"))

if __name__ == "__main__":
    import sys

    pippoo = "we we we"

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
