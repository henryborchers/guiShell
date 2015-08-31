# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/lpsdesk/PycharmProjects/guiShell/gui/basic.ui'
#
# Created: Fri Aug 28 15:43:19 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(721, 478)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.frame = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_start = QtGui.QPushButton(self.frame)
        self.pushButton_start.setEnabled(False)
        self.pushButton_start.setObjectName(_fromUtf8("pushButton_start"))
        self.gridLayout.addWidget(self.pushButton_start, 2, 2, 1, 1)
        self.labelSource = QtGui.QLabel(self.frame)
        self.labelSource.setObjectName(_fromUtf8("labelSource"))
        self.gridLayout.addWidget(self.labelSource, 1, 0, 1, 1)
        self.pushButton_locate = QtGui.QPushButton(self.frame)
        self.pushButton_locate.setObjectName(_fromUtf8("pushButton_locate"))
        self.gridLayout.addWidget(self.pushButton_locate, 1, 2, 1, 1)
        self.lineEditISource = QtGui.QLineEdit(self.frame)
        self.lineEditISource.setObjectName(_fromUtf8("lineEditISource"))
        self.gridLayout.addWidget(self.lineEditISource, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(Form)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.consoleBox = QtGui.QTextEdit(self.frame_2)
        self.consoleBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.consoleBox.setReadOnly(True)
        self.consoleBox.setObjectName(_fromUtf8("consoleBox"))
        self.horizontalLayout.addWidget(self.consoleBox)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButton_start.setText(_translate("Form", "Start", None))
        self.labelSource.setText(_translate("Form", "TextLabel", None))
        self.pushButton_locate.setText(_translate("Form", "Find", None))

