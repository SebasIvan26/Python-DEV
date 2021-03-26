# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI_BASEXjhTXp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 70, 791, 61))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(30)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"background-color: rgb(85, 170, 255);\n"
"border-radius: 20px;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label = QLabel(self.page_home)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 490, 876, 109))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(14)
        self.label.setFont(font6)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.page_home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 360, 876, 109))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(15)
        self.label_7.setFont(font7)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_welcome_usr = QLabel(self.page_home)
        self.label_welcome_usr.setObjectName(u"label_welcome_usr")
        self.label_welcome_usr.setGeometry(QRect(50, 140, 791, 111))
        self.label_welcome_usr.setMinimumSize(QSize(0, 109))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(22)
        self.label_welcome_usr.setFont(font8)
        self.label_welcome_usr.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 8px;\n"
"color: rgb(105, 107, 134)")
        self.label_welcome_usr.setLineWidth(1)
        self.label_welcome_usr.setAlignment(Qt.AlignCenter)
        self.label_time = QLabel(self.page_home)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(50, 230, 791, 51))
        font9 = QFont()
        font9.setFamily(u"Gill Sans")
        font9.setPointSize(29)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_time.setFont(font9)
        self.label_time.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 8px;\n"
"color: rgb(74, 125, 216)")
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.page_home)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 260, 791, 311))
        font10 = QFont()
        font10.setFamily(u"Roboto Thin")
        font10.setPointSize(28)
        font10.setBold(False)
        font10.setWeight(50)
        self.label_4.setFont(font10)
        self.label_4.setStyleSheet(u"background-color: rgb(33, 37, 43);\n"
"border-radius: 10px;\n"
"padding: 5px;\n"
"padding-bottom: 7px;\n"
"margin-top: 8px;\n"
"color: rgb(74, 125, 216)")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setEnabled(True)
        self.labelBoxBlenderInstalation.setGeometry(QRect(12, 2, 281, 31))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(18)
        font11.setBold(True)
        font11.setWeight(75)
        self.labelBoxBlenderInstalation.setFont(font11)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.linebucketEdit = QLineEdit(self.frame_content_wid_1)
        self.linebucketEdit.setObjectName(u"linebucketEdit")
        self.linebucketEdit.setMinimumSize(QSize(0, 30))
        self.linebucketEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.linebucketEdit.setReadOnly(True)
        self.linebucketEdit.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.linebucketEdit, 0, 0, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.bucketpushButton = QPushButton(self.frame_content_wid_1)
        self.bucketpushButton.setObjectName(u"bucketpushButton")
        self.bucketpushButton.setMinimumSize(QSize(150, 30))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        self.bucketpushButton.setFont(font12)
        self.bucketpushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bucketpushButton.setIcon(icon3)

        self.gridLayout.addWidget(self.bucketpushButton, 0, 1, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 150))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 224, 224))
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.plainTextEdit.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 2, 4, 1)

        self.bucketcomboBox = QComboBox(self.frame_2)
        self.bucketcomboBox.addItem("")
        self.bucketcomboBox.addItem("")
        self.bucketcomboBox.setObjectName(u"bucketcomboBox")
        self.bucketcomboBox.setFont(font6)
        self.bucketcomboBox.setAutoFillBackground(False)
        self.bucketcomboBox.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}")
        self.bucketcomboBox.setIconSize(QSize(16, 16))
        self.bucketcomboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.bucketcomboBox, 1, 1, 1, 1)

        self.bucketSaveButton = QPushButton(self.frame_2)
        self.bucketSaveButton.setObjectName(u"bucketSaveButton")
        font13 = QFont()
        font13.setPointSize(10)
        self.bucketSaveButton.setFont(font13)
        self.bucketSaveButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bucketSaveButton.setIcon(icon4)
        self.bucketSaveButton.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.bucketSaveButton, 0, 3, 3, 1)

        self.bucketEIBcheckBox = QCheckBox(self.frame_2)
        self.bucketEIBcheckBox.setObjectName(u"bucketEIBcheckBox")
        self.bucketEIBcheckBox.setFont(font13)
        self.bucketEIBcheckBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.bucketEIBcheckBox, 0, 1, 1, 1)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.bucketRunButton = QPushButton(self.frame_3)
        self.bucketRunButton.setObjectName(u"bucketRunButton")
        font14 = QFont()
        font14.setPointSize(14)
        self.bucketRunButton.setFont(font14)
        self.bucketRunButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/20x20/icons/20x20/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bucketRunButton.setIcon(icon5)
        self.bucketRunButton.setIconSize(QSize(50, 50))

        self.horizontalLayout_12.addWidget(self.bucketRunButton)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)
        self.page_capitalcalc = QWidget()
        self.page_capitalcalc.setObjectName(u"page_capitalcalc")
        self.labelBoxBlenderInstalation_10 = QLabel(self.page_capitalcalc)
        self.labelBoxBlenderInstalation_10.setObjectName(u"labelBoxBlenderInstalation_10")
        self.labelBoxBlenderInstalation_10.setEnabled(True)
        self.labelBoxBlenderInstalation_10.setGeometry(QRect(340, 20, 281, 31))
        font15 = QFont()
        font15.setFamily(u"Segoe UI")
        font15.setPointSize(20)
        font15.setBold(True)
        font15.setWeight(75)
        self.labelBoxBlenderInstalation_10.setFont(font15)
        self.labelBoxBlenderInstalation_10.setStyleSheet(u"")
        self.frame_9 = QFrame(self.page_capitalcalc)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(10, 50, 876, 144))
        self.frame_9.setStyleSheet(u"border-radius: 5px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_9)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_9 = QFrame(self.frame_9)
        self.frame_div_content_9.setObjectName(u"frame_div_content_9")
        self.frame_div_content_9.setMinimumSize(QSize(0, 110))
        self.frame_div_content_9.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_9.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_9.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_div_content_9)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_10 = QFrame(self.frame_div_content_9)
        self.frame_title_wid_10.setObjectName(u"frame_title_wid_10")
        self.frame_title_wid_10.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_10.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_10.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_10.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_11 = QLabel(self.frame_title_wid_10)
        self.labelBoxBlenderInstalation_11.setObjectName(u"labelBoxBlenderInstalation_11")
        self.labelBoxBlenderInstalation_11.setEnabled(True)
        self.labelBoxBlenderInstalation_11.setGeometry(QRect(12, 2, 281, 31))
        font16 = QFont()
        font16.setFamily(u"Segoe UI")
        font16.setPointSize(14)
        font16.setBold(True)
        font16.setWeight(75)
        self.labelBoxBlenderInstalation_11.setFont(font16)
        self.labelBoxBlenderInstalation_11.setStyleSheet(u"")
        self.labelBoxBlenderInstalation_16 = QLabel(self.frame_title_wid_10)
        self.labelBoxBlenderInstalation_16.setObjectName(u"labelBoxBlenderInstalation_16")
        self.labelBoxBlenderInstalation_16.setEnabled(True)
        self.labelBoxBlenderInstalation_16.setGeometry(QRect(600, 0, 281, 31))
        self.labelBoxBlenderInstalation_16.setFont(font1)
        self.labelBoxBlenderInstalation_16.setStyleSheet(u"")

        self.verticalLayout_31.addWidget(self.frame_title_wid_10)

        self.frame_content_wid_10 = QFrame(self.frame_div_content_9)
        self.frame_content_wid_10.setObjectName(u"frame_content_wid_10")
        self.frame_content_wid_10.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_content_wid_10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_10 = QLineEdit(self.frame_content_wid_10)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setMinimumSize(QSize(0, 30))
        self.lineEdit_10.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setClearButtonEnabled(False)

        self.gridLayout_13.addWidget(self.lineEdit_10, 0, 0, 1, 1)

        self.prior_pushButton_2 = QPushButton(self.frame_content_wid_10)
        self.prior_pushButton_2.setObjectName(u"prior_pushButton_2")
        self.prior_pushButton_2.setMinimumSize(QSize(150, 30))
        self.prior_pushButton_2.setFont(font12)
        self.prior_pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.prior_pushButton_2.setIcon(icon3)

        self.gridLayout_13.addWidget(self.prior_pushButton_2, 0, 1, 1, 1)


        self.horizontalLayout_23.addLayout(self.gridLayout_13)


        self.verticalLayout_31.addWidget(self.frame_content_wid_10)


        self.verticalLayout_30.addWidget(self.frame_div_content_9)

        self.frame_10 = QFrame(self.page_capitalcalc)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 160, 876, 144))
        self.frame_10.setStyleSheet(u"border-radius: 5px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_10)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_10 = QFrame(self.frame_10)
        self.frame_div_content_10.setObjectName(u"frame_div_content_10")
        self.frame_div_content_10.setMinimumSize(QSize(0, 110))
        self.frame_div_content_10.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_10.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_10.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_div_content_10)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_11 = QFrame(self.frame_div_content_10)
        self.frame_title_wid_11.setObjectName(u"frame_title_wid_11")
        self.frame_title_wid_11.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_11.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_11.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_11.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_12 = QLabel(self.frame_title_wid_11)
        self.labelBoxBlenderInstalation_12.setObjectName(u"labelBoxBlenderInstalation_12")
        self.labelBoxBlenderInstalation_12.setEnabled(True)
        self.labelBoxBlenderInstalation_12.setGeometry(QRect(12, 2, 281, 31))
        self.labelBoxBlenderInstalation_12.setFont(font16)
        self.labelBoxBlenderInstalation_12.setStyleSheet(u"")

        self.verticalLayout_33.addWidget(self.frame_title_wid_11)

        self.frame_content_wid_11 = QFrame(self.frame_div_content_10)
        self.frame_content_wid_11.setObjectName(u"frame_content_wid_11")
        self.frame_content_wid_11.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_content_wid_11)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit_11 = QLineEdit(self.frame_content_wid_11)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMinimumSize(QSize(0, 30))
        self.lineEdit_11.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setClearButtonEnabled(False)

        self.gridLayout_14.addWidget(self.lineEdit_11, 0, 0, 1, 1)

        self.current_pushButton = QPushButton(self.frame_content_wid_11)
        self.current_pushButton.setObjectName(u"current_pushButton")
        self.current_pushButton.setMinimumSize(QSize(150, 30))
        self.current_pushButton.setFont(font12)
        self.current_pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.current_pushButton.setIcon(icon3)

        self.gridLayout_14.addWidget(self.current_pushButton, 0, 1, 1, 1)


        self.horizontalLayout_24.addLayout(self.gridLayout_14)


        self.verticalLayout_33.addWidget(self.frame_content_wid_11)


        self.verticalLayout_32.addWidget(self.frame_div_content_10)

        self.webCompareButton = QPushButton(self.frame_10)
        self.webCompareButton.setObjectName(u"webCompareButton")
        self.webCompareButton.setMinimumSize(QSize(150, 30))
        self.webCompareButton.setFont(font12)
        self.webCompareButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/20x20/icons/20x20/cil-loop-circular.png", QSize(), QIcon.Normal, QIcon.Off)
        self.webCompareButton.setIcon(icon6)
        self.webCompareButton.setIconSize(QSize(16, 16))

        self.verticalLayout_32.addWidget(self.webCompareButton)

        self.frame_8 = QFrame(self.page_capitalcalc)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(430, 370, 345, 134))
        self.frame_8.setStyleSheet(u"border-radius: 5px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_7 = QFrame(self.frame_8)
        self.frame_div_content_7.setObjectName(u"frame_div_content_7")
        self.frame_div_content_7.setMinimumSize(QSize(0, 110))
        self.frame_div_content_7.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_7.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_7.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_div_content_7)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_8 = QFrame(self.frame_div_content_7)
        self.frame_title_wid_8.setObjectName(u"frame_title_wid_8")
        self.frame_title_wid_8.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_8.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_8.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_8.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_14 = QLabel(self.frame_title_wid_8)
        self.labelBoxBlenderInstalation_14.setObjectName(u"labelBoxBlenderInstalation_14")
        self.labelBoxBlenderInstalation_14.setEnabled(True)
        self.labelBoxBlenderInstalation_14.setGeometry(QRect(10, 0, 281, 31))
        font17 = QFont()
        font17.setFamily(u"Segoe UI")
        font17.setPointSize(16)
        font17.setBold(True)
        font17.setWeight(75)
        self.labelBoxBlenderInstalation_14.setFont(font17)
        self.labelBoxBlenderInstalation_14.setStyleSheet(u"")

        self.verticalLayout_27.addWidget(self.frame_title_wid_8)

        self.frame_content_wid_8 = QFrame(self.frame_div_content_7)
        self.frame_content_wid_8.setObjectName(u"frame_content_wid_8")
        self.frame_content_wid_8.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_content_wid_8)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_12 = QPushButton(self.frame_content_wid_8)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(150, 30))
        self.pushButton_12.setFont(font12)
        self.pushButton_12.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_12.setIcon(icon3)

        self.gridLayout_11.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_content_wid_8)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setMinimumSize(QSize(0, 30))
        self.lineEdit_8.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setClearButtonEnabled(False)

        self.gridLayout_11.addWidget(self.lineEdit_8, 0, 0, 1, 1)

        self.labelVersion_8 = QLabel(self.frame_content_wid_8)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        self.labelVersion_8.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.labelVersion_8, 1, 0, 1, 2)


        self.horizontalLayout_21.addLayout(self.gridLayout_11)


        self.verticalLayout_27.addWidget(self.frame_content_wid_8)


        self.horizontalLayout_25.addWidget(self.frame_div_content_7)

        self.pushButton_17 = QPushButton(self.page_capitalcalc)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(80, 500, 150, 30))
        self.pushButton_17.setMinimumSize(QSize(150, 30))
        self.pushButton_17.setFont(font12)
        self.pushButton_17.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/16x16/icons/16x16/cil-loop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_17.setIcon(icon7)
        self.pushButton_17.setIconSize(QSize(16, 16))
        self.frame_11 = QFrame(self.page_capitalcalc)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(80, 370, 345, 134))
        self.frame_11.setStyleSheet(u"border-radius: 5px;")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_8 = QFrame(self.frame_11)
        self.frame_div_content_8.setObjectName(u"frame_div_content_8")
        self.frame_div_content_8.setMinimumSize(QSize(0, 110))
        self.frame_div_content_8.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_8.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_8.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_div_content_8)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_9 = QFrame(self.frame_div_content_8)
        self.frame_title_wid_9.setObjectName(u"frame_title_wid_9")
        self.frame_title_wid_9.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_9.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_9.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_9.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_15 = QLabel(self.frame_title_wid_9)
        self.labelBoxBlenderInstalation_15.setObjectName(u"labelBoxBlenderInstalation_15")
        self.labelBoxBlenderInstalation_15.setEnabled(True)
        self.labelBoxBlenderInstalation_15.setGeometry(QRect(10, 0, 281, 31))
        self.labelBoxBlenderInstalation_15.setFont(font17)
        self.labelBoxBlenderInstalation_15.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.frame_title_wid_9)

        self.frame_content_wid_9 = QFrame(self.frame_div_content_8)
        self.frame_content_wid_9.setObjectName(u"frame_content_wid_9")
        self.frame_content_wid_9.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_content_wid_9)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_13 = QPushButton(self.frame_content_wid_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(150, 30))
        self.pushButton_13.setFont(font12)
        self.pushButton_13.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_13.setIcon(icon3)

        self.gridLayout_12.addWidget(self.pushButton_13, 0, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_content_wid_9)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setMinimumSize(QSize(0, 30))
        self.lineEdit_9.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setClearButtonEnabled(False)

        self.gridLayout_12.addWidget(self.lineEdit_9, 0, 0, 1, 1)

        self.labelVersion_9 = QLabel(self.frame_content_wid_9)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        self.labelVersion_9.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.labelVersion_9, 1, 0, 1, 2)


        self.horizontalLayout_22.addLayout(self.gridLayout_12)


        self.verticalLayout_28.addWidget(self.frame_content_wid_9)


        self.horizontalLayout_26.addWidget(self.frame_div_content_8)

        self.stackedWidget.addWidget(self.page_capitalcalc)
        self.page_cash_flow_file = QWidget()
        self.page_cash_flow_file.setObjectName(u"page_cash_flow_file")
        self.frame_4 = QFrame(self.page_cash_flow_file)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(20, 0, 876, 144))
        self.frame_4.setStyleSheet(u"border-radius: 5px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_2 = QFrame(self.frame_4)
        self.frame_div_content_2.setObjectName(u"frame_div_content_2")
        self.frame_div_content_2.setMinimumSize(QSize(0, 110))
        self.frame_div_content_2.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_2.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_2.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_div_content_2)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.labelBoxBlenderInstalation_2 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setEnabled(True)
        self.labelBoxBlenderInstalation_2.setGeometry(QRect(12, 2, 281, 31))
        self.labelBoxBlenderInstalation_2.setFont(font11)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.frame_title_wid_2)

        self.frame_content_wid_2 = QFrame(self.frame_div_content_2)
        self.frame_content_wid_2.setObjectName(u"frame_content_wid_2")
        self.frame_content_wid_2.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_content_wid_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.linecashflowtEdit_2 = QLineEdit(self.frame_content_wid_2)
        self.linecashflowtEdit_2.setObjectName(u"linecashflowtEdit_2")
        self.linecashflowtEdit_2.setMinimumSize(QSize(0, 30))
        self.linecashflowtEdit_2.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.linecashflowtEdit_2.setReadOnly(True)
        self.linecashflowtEdit_2.setClearButtonEnabled(False)

        self.gridLayout_3.addWidget(self.linecashflowtEdit_2, 0, 0, 1, 1)

        self.labelVersion_4 = QLabel(self.frame_content_wid_2)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        self.labelVersion_4.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.labelVersion_4, 1, 0, 1, 2)

        self.cash_flow_pushButton_2 = QPushButton(self.frame_content_wid_2)
        self.cash_flow_pushButton_2.setObjectName(u"cash_flow_pushButton_2")
        self.cash_flow_pushButton_2.setMinimumSize(QSize(150, 30))
        self.cash_flow_pushButton_2.setFont(font12)
        self.cash_flow_pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.cash_flow_pushButton_2.setIcon(icon3)

        self.gridLayout_3.addWidget(self.cash_flow_pushButton_2, 0, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout_3)


        self.verticalLayout_8.addWidget(self.frame_content_wid_2)


        self.verticalLayout_16.addWidget(self.frame_div_content_2)

        self.frame_5 = QFrame(self.page_cash_flow_file)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(20, 150, 876, 250))
        self.frame_5.setMinimumSize(QSize(0, 150))
        self.frame_5.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cash_flow_generate_button = QPushButton(self.frame_5)
        self.cash_flow_generate_button.setObjectName(u"cash_flow_generate_button")
        self.cash_flow_generate_button.setFont(font13)
        self.cash_flow_generate_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/16x16/icons/16x16/cil-media-play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cash_flow_generate_button.setIcon(icon8)
        self.cash_flow_generate_button.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.cash_flow_generate_button, 0, 1, 1, 1)

        self.scrollArea_2 = QScrollArea(self.frame_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")
        self.scrollArea_2.setFrameShape(QFrame.NoFrame)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 552, 224))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.cash_flow_plainTextEdit_2 = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.cash_flow_plainTextEdit_2.setObjectName(u"cash_flow_plainTextEdit_2")
        self.cash_flow_plainTextEdit_2.setMinimumSize(QSize(200, 200))
        self.cash_flow_plainTextEdit_2.setStyleSheet(u"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"}\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.cash_flow_plainTextEdit_2.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.cash_flow_plainTextEdit_2)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 0, 2, 3, 1)

        self.cashflow_savebutton = QPushButton(self.frame_5)
        self.cashflow_savebutton.setObjectName(u"cashflow_savebutton")
        self.cashflow_savebutton.setFont(font13)
        self.cashflow_savebutton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.cashflow_savebutton.setIcon(icon4)
        self.cashflow_savebutton.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.cashflow_savebutton, 0, 3, 2, 1)

        self.cash_flow_getstats_button = QPushButton(self.frame_5)
        self.cash_flow_getstats_button.setObjectName(u"cash_flow_getstats_button")
        self.cash_flow_getstats_button.setFont(font13)
        self.cash_flow_getstats_button.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/16x16/icons/16x16/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cash_flow_getstats_button.setIcon(icon9)
        self.cash_flow_getstats_button.setIconSize(QSize(50, 50))

        self.gridLayout_4.addWidget(self.cash_flow_getstats_button, 1, 1, 1, 1)


        self.verticalLayout_12.addLayout(self.gridLayout_4)

        self.stackedWidget.addWidget(self.page_cash_flow_file)
        self.page_cash = QWidget()
        self.page_cash.setObjectName(u"page_cash")
        self.cash_calendar = QCalendarWidget(self.page_cash)
        self.cash_calendar.setObjectName(u"cash_calendar")
        self.cash_calendar.setGeometry(QRect(600, 70, 271, 151))
        self.cash_calendar.setMouseTracking(True)
        self.cash_calendar.setTabletTracking(True)
        self.cash_calendar.setAutoFillBackground(False)
        self.cash_calendar.setSelectedDate(QDate(2021, 3, 1))
        self.cash_calendar.setFirstDayOfWeek(Qt.Sunday)
        self.cash_calendar.setGridVisible(False)
        self.cash_calendar.setHorizontalHeaderFormat(QCalendarWidget.ShortDayNames)
        self.cash_calendar.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.cash_calendar.setNavigationBarVisible(True)
        self.cash_calendar.setDateEditEnabled(True)
        self.commandLinkButton_2 = QCommandLinkButton(self.page_cash)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(720, 280, 168, 42))
        self.commandLinkButton_2.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/16x16/icons/16x16/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_2.setIcon(icon10)
        self.labelBoxBlenderInstalation_13 = QLabel(self.page_cash)
        self.labelBoxBlenderInstalation_13.setObjectName(u"labelBoxBlenderInstalation_13")
        self.labelBoxBlenderInstalation_13.setEnabled(True)
        self.labelBoxBlenderInstalation_13.setGeometry(QRect(310, 10, 431, 51))
        font18 = QFont()
        font18.setFamily(u"Segoe UI")
        font18.setPointSize(22)
        font18.setBold(True)
        font18.setWeight(75)
        self.labelBoxBlenderInstalation_13.setFont(font18)
        self.labelBoxBlenderInstalation_13.setStyleSheet(u"")
        self.pushButton_19 = QPushButton(self.page_cash)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(20, 240, 271, 54))
        self.pushButton_19.setFont(font14)
        self.pushButton_19.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 4rgb(64, 152, 255)9);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/20x20/icons/20x20/cil-reload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon11)
        self.pushButton_19.setIconSize(QSize(50, 50))
        self.calendar_label = QLabel(self.page_cash)
        self.calendar_label.setObjectName(u"calendar_label")
        self.calendar_label.setGeometry(QRect(640, 240, 191, 31))
        self.calendar_label.setStyleSheet(u"QLabel {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.dateEdit = QDateEdit(self.page_cash)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(50, 110, 110, 22))
        self.lineEdit_12 = QLineEdit(self.page_cash)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setGeometry(QRect(40, 170, 181, 21))
        self.lineEdit_13 = QLineEdit(self.page_cash)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setGeometry(QRect(40, 200, 181, 21))
        self.cashTableWidget = QTableWidget(self.page_cash)
        if (self.cashTableWidget.columnCount() < 4):
            self.cashTableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.cashTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cashTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cashTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cashTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.cashTableWidget.rowCount() < 16):
            self.cashTableWidget.setRowCount(16)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.cashTableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.cashTableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.cashTableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.cashTableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.cashTableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.cashTableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.cashTableWidget.setObjectName(u"cashTableWidget")
        self.cashTableWidget.setGeometry(QRect(15, 325, 871, 261))
        sizePolicy.setHeightForWidth(self.cashTableWidget.sizePolicy().hasHeightForWidth())
        self.cashTableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        self.cashTableWidget.setPalette(palette1)
        self.cashTableWidget.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.cashTableWidget.setFrameShape(QFrame.NoFrame)
        self.cashTableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.cashTableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.cashTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cashTableWidget.setAlternatingRowColors(False)
        self.cashTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.cashTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cashTableWidget.setShowGrid(True)
        self.cashTableWidget.setGridStyle(Qt.SolidLine)
        self.cashTableWidget.setSortingEnabled(False)
        self.cashTableWidget.horizontalHeader().setVisible(False)
        self.cashTableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.cashTableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.cashTableWidget.horizontalHeader().setStretchLastSection(True)
        self.cashTableWidget.verticalHeader().setVisible(False)
        self.cashTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.cashTableWidget.verticalHeader().setHighlightSections(False)
        self.cashTableWidget.verticalHeader().setStretchLastSection(True)
        self.stackedWidget.addWidget(self.page_cash)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
        QWidget.setTabOrder(self.btn_toggle_menu, self.bucketEIBcheckBox)
        QWidget.setTabOrder(self.bucketEIBcheckBox, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
        QWidget.setTabOrder(self.plainTextEdit, self.bucketSaveButton)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - GA Lab", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"Wellington Management Company", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| Lab", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"GA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.label.setText("")
        self.label_7.setText("")
        self.label_welcome_usr.setText(QCoreApplication.translate("MainWindow", u"Welcome, ", None))
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.label_4.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Bucket Report", None))
        self.linebucketEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose File", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program FilesBlender FoundationBlender 2.82 blender.exe", None))
        self.bucketpushButton.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.bucketcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"STAT AUM                    ", None))
        self.bucketcomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"STAT REV", None))

        self.bucketSaveButton.setText(QCoreApplication.translate("MainWindow", u"Saving location", None))
        self.bucketEIBcheckBox.setText(QCoreApplication.translate("MainWindow", u"Generate EIB                            ", None))
        self.bucketRunButton.setText(QCoreApplication.translate("MainWindow", u"Run Report", None))
        self.labelBoxBlenderInstalation_10.setText(QCoreApplication.translate("MainWindow", u"Comparator", None))
        self.labelBoxBlenderInstalation_11.setText(QCoreApplication.translate("MainWindow", u"Version 1 : ", None))
        self.labelBoxBlenderInstalation_16.setText(QCoreApplication.translate("MainWindow", u"*Supported formats: PDF,  Excel,  Word", None))
        self.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter File", None))
        self.prior_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelBoxBlenderInstalation_12.setText(QCoreApplication.translate("MainWindow", u"Version 2 : ", None))
        self.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter File", None))
        self.current_pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.webCompareButton.setText(QCoreApplication.translate("MainWindow", u"Compare", None))
        self.labelBoxBlenderInstalation_14.setText(QCoreApplication.translate("MainWindow", u"Time Series - WM Canada", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Time Series File", None))
        self.labelVersion_8.setText(QCoreApplication.translate("MainWindow", u"Update Time Series - Capital Cal", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"Update Time Series Calc", None))
        self.labelBoxBlenderInstalation_15.setText(QCoreApplication.translate("MainWindow", u"Capital Calculation - WM Canada", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Capital Calc File", None))
        self.labelVersion_9.setText(QCoreApplication.translate("MainWindow", u"Update Time Series - Capital Cal", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"WTC Cash Flow File", None))
        self.linecashflowtEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Cash Flow File", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Ex: C:Program Files\\WTC\\Cash Flow Files.xlsx", None))
        self.cash_flow_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.cash_flow_generate_button.setText(QCoreApplication.translate("MainWindow", u"Generate File", None))
        self.cashflow_savebutton.setText(QCoreApplication.translate("MainWindow", u"Saving location", None))
        self.cash_flow_getstats_button.setText(QCoreApplication.translate("MainWindow", u"Get Statistics", None))
        self.commandLinkButton_2.setText(QCoreApplication.translate("MainWindow", u"CommandLinkButton", None))
        self.commandLinkButton_2.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
        self.labelBoxBlenderInstalation_13.setText(QCoreApplication.translate("MainWindow", u"Cash Finder", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"Find Cash ", None))
        self.calendar_label.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.lineEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount greater than", None))
        self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount less than", None))
        ___qtablewidgetitem = self.cashTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.cashTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.cashTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.cashTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.cashTableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.cashTableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.cashTableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.cashTableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.cashTableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.cashTableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.cashTableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.cashTableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.cashTableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.cashTableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.cashTableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.cashTableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.cashTableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.cashTableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.cashTableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.cashTableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.cashTableWidget.isSortingEnabled()
        self.cashTableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.cashTableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.cashTableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.cashTableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.cashTableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.cashTableWidget.setSortingEnabled(__sortingEnabled)

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Global-Accounting", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

