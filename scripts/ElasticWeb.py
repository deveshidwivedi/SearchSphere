# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ElasticWeb.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.verticalLayout.addWidget(self.checkBox_1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout.addWidget(self.checkBox_5)
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout.addWidget(self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout.addWidget(self.checkBox_8)
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout.addWidget(self.checkBox_10)
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout.addWidget(self.checkBox_11)
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout.addWidget(self.checkBox_12)
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout.addWidget(self.checkBox_14)
        '''self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout.addWidget(self.checkBox_9)'''
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout.addWidget(self.checkBox_15)
        self.checkBox_17 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout.addWidget(self.checkBox_17)
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout.addWidget(self.checkBox_13)
        '''self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout.addWidget(self.checkBox_16)'''
        '''self.checkBox_18 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout.addWidget(self.checkBox_18)'''
        self.checkBox_19 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout.addWidget(self.checkBox_19)
        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ElasticWeb"))
        self.label_2.setText(_translate("MainWindow", "Elastic Nptel WebSite CourseFinder"))
        self.label.setText(_translate("MainWindow", "Search Course  : "))
        self.checkBox_1.setText(_translate("MainWindow", "Aerospace Engineering"))
        self.checkBox_3.setText(_translate("MainWindow", "Agricultural and Food Engineering"))
        self.checkBox_2.setText(_translate("MainWindow", "Architecture and Planning"))
        self.checkBox_4.setText(_translate("MainWindow", "Biological Sciences & Bioengineering"))
        self.checkBox_5.setText(_translate("MainWindow", "Chemical Engineering"))
        self.checkBox_6.setText(_translate("MainWindow", "Maths and Sciences"))
        self.checkBox_7.setText(_translate("MainWindow", "Civil Engineering"))
        self.checkBox_8.setText(_translate("MainWindow", "Computer Science and Engineering"))
        self.checkBox_10.setText(_translate("MainWindow", "Design Engineering"))
        self.checkBox_11.setText(_translate("MainWindow", "Electrical, Electronics and Communications Engineering"))
        self.checkBox_12.setText(_translate("MainWindow", "Humanities and Social Sciences"))
        self.checkBox_14.setText(_translate("MainWindow", "Management"))
        self.checkBox_15.setText(_translate("MainWindow", "Mechanical Engineering"))
        self.checkBox_17.setText(_translate("MainWindow", "Metallurgy and Material sciences & Mining Engineering"))
        self.checkBox_13.setText(_translate("MainWindow", "Multidisciplinary"))
        self.checkBox_19.setText(_translate("MainWindow", "Textile Engineering"))

