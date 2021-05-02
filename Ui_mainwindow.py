# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(743, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMaximumSize(QSize(800, 800))
        self.gridLayout = QGridLayout(mainWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.idxBox = QLineEdit(mainWindow)
        self.idxBox.setObjectName(u"idxBox")
        self.idxBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.idxBox.sizePolicy().hasHeightForWidth())
        self.idxBox.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(15)
        self.idxBox.setFont(font)

        self.gridLayout.addWidget(self.idxBox, 0, 0, 1, 1)

        self.gotoButton = QPushButton(mainWindow)
        self.gotoButton.setObjectName(u"gotoButton")
        self.gotoButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.gotoButton.sizePolicy().hasHeightForWidth())
        self.gotoButton.setSizePolicy(sizePolicy1)
        self.gotoButton.setFont(font)

        self.gridLayout.addWidget(self.gotoButton, 0, 1, 1, 1)

        self.fileNameBox = QTextBrowser(mainWindow)
        self.fileNameBox.setObjectName(u"fileNameBox")

        self.gridLayout.addWidget(self.fileNameBox, 0, 2, 1, 1)

        self.playButton = QPushButton(mainWindow)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.playButton.sizePolicy().hasHeightForWidth())
        self.playButton.setSizePolicy(sizePolicy1)
        self.playButton.setFont(font)

        self.gridLayout.addWidget(self.playButton, 0, 3, 1, 1)

        self.labelBox = QTextEdit(mainWindow)
        self.labelBox.setObjectName(u"labelBox")

        self.gridLayout.addWidget(self.labelBox, 1, 0, 1, 3)

        self.saveButton = QPushButton(mainWindow)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy1)
        self.saveButton.setFont(font)

        self.gridLayout.addWidget(self.saveButton, 1, 3, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.backButton = QPushButton(mainWindow)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy1)
        self.backButton.setFont(font)

        self.horizontalLayout.addWidget(self.backButton)

        self.nextButton = QPushButton(mainWindow)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy1)
        self.nextButton.setFont(font)

        self.horizontalLayout.addWidget(self.nextButton)

        self.delButton = QPushButton(mainWindow)
        self.delButton.setObjectName(u"delButton")
        self.delButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.delButton.sizePolicy().hasHeightForWidth())
        self.delButton.setSizePolicy(sizePolicy1)
        self.delButton.setFont(font)

        self.horizontalLayout.addWidget(self.delButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)


        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"mainWindow", None))
        self.gotoButton.setText(QCoreApplication.translate("mainWindow", u"Goto", None))
        self.playButton.setText(QCoreApplication.translate("mainWindow", u"Play", None))
        self.saveButton.setText(QCoreApplication.translate("mainWindow", u"Save", None))
        self.backButton.setText(QCoreApplication.translate("mainWindow", u"Back", None))
        self.nextButton.setText(QCoreApplication.translate("mainWindow", u"Next", None))
        self.delButton.setText(QCoreApplication.translate("mainWindow", u"Delete this image", None))
    # retranslateUi

