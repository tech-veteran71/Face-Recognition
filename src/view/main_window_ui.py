# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\src\ui\main_window_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from .resources_rc import *
from PyQt5 import QtCore, QtGui, QtWidgets
from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 720)
        MainWindow.setMinimumSize(QtCore.QSize(640, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainWindow/images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Main_frame = QtWidgets.QFrame(self.centralwidget)
        self.Main_frame.setObjectName("Main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Main_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttons_frame = QtWidgets.QFrame(self.Main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_frame.sizePolicy().hasHeightForWidth())
        self.buttons_frame.setSizePolicy(sizePolicy)
        self.buttons_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.buttons_frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.buttons_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttons_frame.setAutoFillBackground(False)
        self.buttons_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.buttons_frame.setObjectName("buttons_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.buttons_frame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.webcam_radioButton = QtWidgets.QRadioButton(self.buttons_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webcam_radioButton.setFont(font)
        self.webcam_radioButton.setAutoFillBackground(False)
        self.webcam_radioButton.setIconSize(QtCore.QSize(16, 16))
        self.webcam_radioButton.setChecked(True)
        self.webcam_radioButton.setObjectName("webcam_radioButton")
        self.verticalLayout.addWidget(self.webcam_radioButton)
        self.video_radioButton = QtWidgets.QRadioButton(self.buttons_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.video_radioButton.setFont(font)
        self.video_radioButton.setObjectName("video_radioButton")
        self.verticalLayout.addWidget(self.video_radioButton)
        self.loadimages_pushButton = QtWidgets.QPushButton(self.buttons_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loadimages_pushButton.setFont(font)
        self.loadimages_pushButton.setObjectName("loadimages_pushButton")
        self.verticalLayout.addWidget(self.loadimages_pushButton)
        self.loadvideo_pushButton = QtWidgets.QPushButton(self.buttons_frame)
        self.loadvideo_pushButton.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.loadvideo_pushButton.setFont(font)
        self.loadvideo_pushButton.setObjectName("loadvideo_pushButton")
        self.verticalLayout.addWidget(self.loadvideo_pushButton)
        self.parametres_pushButton = QtWidgets.QPushButton(self.buttons_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.parametres_pushButton.setFont(font)
        self.parametres_pushButton.setObjectName("parametres_pushButton")
        self.verticalLayout.addWidget(self.parametres_pushButton)
        self.recognise_pushButton = QtWidgets.QPushButton(self.buttons_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.recognise_pushButton.setFont(font)
        self.recognise_pushButton.setObjectName("recognise_pushButton")
        self.verticalLayout.addWidget(self.recognise_pushButton)
        self.horizontalLayout.addWidget(self.buttons_frame, 0, QtCore.Qt.AlignTop)
        self.webcam_groupBox = QtWidgets.QGroupBox(self.Main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webcam_groupBox.sizePolicy().hasHeightForWidth())
        self.webcam_groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.webcam_groupBox.setFont(font)
        self.webcam_groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.webcam_groupBox.setFlat(False)
        self.webcam_groupBox.setObjectName("webcam_groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.webcam_groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Web_label_2 = QtWidgets.QLabel(self.webcam_groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Web_label_2.sizePolicy().hasHeightForWidth())
        self.Web_label_2.setSizePolicy(sizePolicy)
        self.Web_label_2.setText("")
        self.Web_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.Web_label_2.setWordWrap(False)
        self.Web_label_2.setObjectName("Web_label_2")
        self.horizontalLayout_2.addWidget(self.Web_label_2)
        self.horizontalLayout.addWidget(self.webcam_groupBox)
        self.gridLayout.addWidget(self.Main_frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1020, 21))
        self.menuBar.setObjectName("menuBar")
        self.About_menu = QtWidgets.QMenu(self.menuBar)
        self.About_menu.setObjectName("About_menu")
        MainWindow.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.About_menu.menuAction())
        self.designers_action = QtWidgets.QAction("Информация о разработчиках")
        self.inf_action = QtWidgets.QAction("Описание приложения")
        self.About_menu.addAction(self.designers_action)
        self.About_menu.addAction(self.inf_action)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Распознание личности"))
        self.webcam_radioButton.setText(_translate("MainWindow", "Веб-камера"))
        self.video_radioButton.setText(_translate("MainWindow", "Видео"))
        self.loadimages_pushButton.setText(_translate("MainWindow", "Загрузить личность"))
        self.loadvideo_pushButton.setText(_translate("MainWindow", "Загрузить видео"))
        self.parametres_pushButton.setText(_translate("MainWindow", "Параметры"))
        self.recognise_pushButton.setText(_translate("MainWindow", "Распознать"))
        self.webcam_groupBox.setTitle(_translate("MainWindow", "Веб-камера"))
        self.About_menu.setTitle(_translate("MainWindow", "О программе"))