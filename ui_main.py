# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QTextBrowser,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        icon = QIcon()
        icon.addFile(u":/images/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(120, 0))

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(120, 0))
        self.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(160, 0))

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(160, 0))

        self.gridLayout_2.addWidget(self.comboBox_2, 1, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(120, 0))

        self.gridLayout_2.addWidget(self.lineEdit_4, 1, 3, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit_5 = QLineEdit(self.groupBox_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_4 = QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_4.addWidget(self.lineEdit_6, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_4.addWidget(self.pushButton_2, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_5 = QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.textBrowser = QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox_6)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox_6)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_2.addWidget(self.pushButton_7)


        self.horizontalLayout_2.addWidget(self.groupBox_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.verticalLayout = QVBoxLayout(self.groupBox_7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser_2 = QTextBrowser(self.groupBox_7)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.verticalLayout.addWidget(self.textBrowser_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.progressBar = QProgressBar(self.groupBox_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar)

        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.progressBar_2 = QProgressBar(self.groupBox_7)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.horizontalLayout_3.addWidget(self.progressBar_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_7)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CDSE \u6570\u636e\u4e0b\u8f7d\u5de5\u5177 v2.0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"CDSE \u8d26\u53f7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801\uff1a", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bbe\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u536b\u661f\u5e73\u53f0\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u59cb\u65e5\u671f\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4ea7\u54c1\u7c7b\u578b\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u622a\u6b62\u65e5\u671f\uff1a", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"GeoJSON\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4f4d\u7f6e", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u67e5\u8be2", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u63a7\u5236\u9762\u677f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u72b6\u6001", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u6587\u4ef6\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6240\u6709\u6587\u4ef6\u4e0b\u8f7d\u8fdb\u5ea6\uff1a", None))
    # retranslateUi

