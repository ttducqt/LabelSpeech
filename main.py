# This Python file uses the following encoding: utf-8
import os
import sys
import codecs
from playsound import playsound

import PySide2
from PySide2.QtCore import QFile, Qt, QThreadPool, QRunnable
from PySide2.QtGui import QImage, QKeySequence
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QShortcut, QSizePolicy

from Ui_mainwindow import Ui_mainWindow

PySide2.QtCore.Qt.Key

class Runnable(QRunnable):
    def __init__(self, fpath):
        super().__init__()
        self.fpath = fpath
    
    def run(self):
        playsound(self.fpath)


class mainWindow(QWidget):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        #sub-folder inside is OK
        self.sound_dir = '/home/duc/Desktop/ML_WorkSpace/tools/LabelSpeech/test_data/VIVOSDEV01'
        self.list_file = tuple(os.walk(self.sound_dir))[0][2]

        #auto create labels.txt by the path
        self.label_path = 'test_data/labels.txt'
        with codecs.open(self.label_path, 'r+', encoding='utf8') as f:
            self.anno_list = [line.replace('\n','').split('\t') for line in f]
            if not len(self.anno_list):
                self.anno_list = [[f,''] for f in self.list_file]


        self.index = 0
        self.updateScreen()

        self.ui.saveButton.clicked.connect(self.saveFn)
        self.ui.nextButton.setShortcut('s')

        self.ui.nextButton.clicked.connect(self.nextFn)
        self.ui.nextButton.setShortcut('d')

        self.ui.backButton.clicked.connect(self.backFn)
        self.ui.backButton.setShortcut('a')

        self.ui.delButton.clicked.connect(self.delFn)
        self.ui.saveButton.setShortcut('del')

        self.ui.gotoButton.clicked.connect(self.gotoFn)
        self.ui.playButton.clicked.connect(self.playSound)

    def playSound(self):
        playsound(os.path.join(self.sound_dir, self.anno_list[self.index][0]))

    def updateScreen(self):
        if abs(self.index) >= len(self.anno_list):
            self.index = 0

        self.ui.fileNameBox.setText(
            str(os.path.join(self.sound_dir,self.anno_list[self.index][0])))

        self.ui.labelBox.setText(self.anno_list[self.index][1])
        self.ui.idxBox.setText(str(self.index))


    def checkEdit(self):
        if self.ui.labelBox.toPlainText() != self.anno_list[self.index][1]:
            self.anno_list[self.index][1] = self.ui.labelBox.toPlainText()

    def nextFn(self):
        self.checkEdit()
        self.index += 1
        self.updateScreen()
    
    def backFn(self):
        self.checkEdit()
        self.index -= 1
        self.updateScreen()
    
    def saveFn(self):
        self.checkEdit()
        self.ui.saveButton.setText('Saving')
        with codecs.open(os.path.join(self.label_path),
                        'w+', encoding='utf8') as f:
            for line in self.anno_list:
                f.write('\t'.join(line)+'\n')
        
        self.ui.saveButton.setText('Save')

    def delFn(self):
        os.remove(os.path.join(self.sound_dir, self.anno_list[self.index][0]))
        del(self.anno_list[self.index])
        self.updateScreen()
    
    def gotoFn(self):
        self.index = int(self.ui.idxBox.text())
        self.updateScreen()


if __name__ == "__main__":
    app = QApplication([])
    widget = mainWindow()
    widget.show()
    sys.exit(app.exec_())
