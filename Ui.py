import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QSize

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color : black;")
        self.resize(1600, 900)
        self.centralWidget = QtWidgets.QWidget(self)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.pageList = []
        for i in range(0,4):
            page = QtWidgets.QWidget()
            self.pageList.append(page)
            self.stackedWidget.addWidget(self.pageList[i])
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1600, 900))
        self.signInPageUi()
        self.signUpPageUi()
        self.playListPageUi()
        self.videoPageUi()
        self.setCentralWidget(self.centralWidget)
        self.show()


    def signInPageUi(self):
        self.signIpBtnList = []
        btn = QtWidgets.QPushButton(self.pageList[0])
        btn.setGeometry(QtCore.QRect(650,640,300,50))
        btn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "border-radius: 5px;\n"
                "color : white;"
                "font-size: 20pt;")
        btn.setText("Sign In")
        self.signIpBtnList.append(btn)

        btn = QtWidgets.QPushButton(self.pageList[0])
        btn.setGeometry(QtCore.QRect(600,820,400,30))
        btn.setStyleSheet("border-radius: 5px;\n"
                "color : white;"
                "font-size: 16pt;")
        btn.setText("Don't have an ID? click here to Sign Up")
        self.signIpBtnList.append(btn)    
        
        self.signInLineEditList = []
        for i in range(0,2):
                lineEdit = QtWidgets.QLineEdit(self.pageList[0])
                lineEdit.setGeometry(QtCore.QRect(650,510+60*i,300,50))
                lineEdit.setStyleSheet(
                    "background-color : rgb(50,50,50);"
                    "padding-left : 20px;"
                    "border-radius: 5px;"
                    "font-size: 16pt;"
                    "color : white;")
                self.signInLineEditList.append(lineEdit)
        self.signInLineEditList[0].setPlaceholderText("User ID")
        self.signInLineEditList[1].setPlaceholderText("PassWord")
        self.signInLineEditList[1].setEchoMode(QtWidgets.QLineEdit.Password)
        
        label = QtWidgets.QLabel(self.pageList[0])
        label.setGeometry(QtCore.QRect(900, 620, 60, 20))
        label.setText("test")
        label.setStyleSheet("color: red;\n"
            "font-size: 13pt;")

        logoImage = QtWidgets.QPushButton(self.pageList[0])
        logoImage.setGeometry(QtCore.QRect(675,180,250,250))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("stageUsLogo.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        logoImage.setIcon(icon)
        logoImage.setIconSize(QtCore.QSize(250, 250))
        
         

    def signUpPageUi(self):
        self.signUpBtnList = []
        signUpBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpBtn.setGeometry(QtCore.QRect(650,520,300,50))
        signUpBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "border-radius: 5px;\n"
                "color : white;"
                "font-size: 20pt;")
        signUpBtn.setText("Sign In")
        self.signUpBtnList.append(signUpBtn)

        signUpCheckBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpCheckBtn.setGeometry(QtCore.QRect(870,280,80,50))
        signUpCheckBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 5px;\n"
                "color : white;\n"
                "font-size: 13pt;")
        signUpCheckBtn.setText("Check")
        self.signUpBtnList.append(signUpCheckBtn)

        signUpBackBtn = QtWidgets.QPushButton(self.pageList[1])
        signUpBackBtn.setGeometry(QtCore.QRect(1450,20,113,32))
        signUpBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 10px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        signUpBackBtn.setText("< Back")
        self.signUpBtnList.append(signUpBackBtn)   
        

        self.signUpLineEditList = []
        lineEdit = QtWidgets.QLineEdit(self.pageList[1])
        lineEdit.setGeometry(QtCore.QRect(650,280,215,50))
        lineEdit.setStyleSheet(
            "background-color : rgb(50,50,50);"
            "padding-left : 20px;"
            "border-radius: 5px;"
            "font-size: 20pt;"
            "color : white;")
        self.signUpLineEditList.append(lineEdit)

        for i in range(0,3):
                lineEdit = QtWidgets.QLineEdit(self.pageList[1])
                lineEdit.setGeometry(QtCore.QRect(650,340+60*i,300,50))
                lineEdit.setStyleSheet(
                    "background-color : rgb(50,50,50);"
                    "padding-left : 20px;"
                    "border-radius: 5px;"
                    "font-size: 20pt;"
                    "color : white;")
                self.signUpLineEditList.append(lineEdit)

        self.signUpLineEditList[0].setPlaceholderText("User ID")
        self.signUpLineEditList[1].setPlaceholderText("Name")
        self.signUpLineEditList[2].setPlaceholderText("PassWord")
        self.signUpLineEditList[3].setPlaceholderText("PassWord Check")
        for i in range(0,2):
            self.signUpLineEditList[i+2].setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.idCheckLabel = QtWidgets.QLabel(self.pageList[1])
        self.idCheckLabel.setGeometry(QtCore.QRect(810, 295, 45, 20))
        self.idCheckLabel.setText("Invalid")
        self.idCheckLabel.setStyleSheet("color: red;\n"
            "background-color : rgb(50,50,50);\n"
            "font-size: 13pt;")

        

    def playListPageUi(self):
        self.playListScroll = QtWidgets.QScrollArea(self.pageList[2])
        self.playListWidget = QtWidgets.QWidget()
        self.playListVbox = QtWidgets.QVBoxLayout() 

        self.playListScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.playListScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.playListScroll.setWidgetResizable(True)
        self.playListScroll.setGeometry(QtCore.QRect(550,100,540,800))

        for i in range(1,10):
            btn = QtWidgets.QWidget()
            btn.setFixedWidth(500)
            btn.setFixedHeight(100)
            btn.setStyleSheet("background-color : rgb(30,30,30);\n"
                    #"color : white;\n"
                    #"padding-right : 50px;\n"
                    "border-radius: 8px;\n")
            self.playListVbox.addWidget(btn)
        
        self.playListWidget.setLayout(self.playListVbox)
        self.playListScroll.setWidget(self.playListWidget)


        self.idLabel = QtWidgets.QLabel(self.pageList[2])
        self.idLabel.setGeometry(QtCore.QRect(50, 20, 140, 20))
        self.idLabel.setStyleSheet(
                "color : white;"
                "font-size: 13pt;")
        self.idLabel.setText("님 환영합니다!")

        self.playListBtnList = []
        playListBackBtn = QtWidgets.QPushButton(self.pageList[2])
        playListBackBtn.setGeometry(QtCore.QRect(1450,20,113,32))
        playListBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 4px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        playListBackBtn.setText("< Back")
        self.playListBtnList.append(playListBackBtn)   

        playListAddBtn = QtWidgets.QPushButton(self.pageList[2])
        playListAddBtn.setGeometry(QtCore.QRect(1320,20,113,32))
        playListAddBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "padding-left : 2px;\n"
                "font-size: 13pt;\n"
                "border-radius: 4px;\n"
                "color : white;")
        playListAddBtn.setText("+ Add PlayList")
        self.playListBtnList.append(playListAddBtn)




    def videoPageUi(self):
        #스크롤
        self.videoScroll = QtWidgets.QScrollArea(self.pageList[3])
        self.videoListWidget = QtWidgets.QWidget()
        self.videpListVbox = QtWidgets.QVBoxLayout() 

        self.videoScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.videoScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.videoScroll.setWidgetResizable(True)
        self.videoScroll.setGeometry(QtCore.QRect(1300,60,290,1000))

        for i in range(1,100):
            btn = QtWidgets.QWidget()
            btn.setFixedWidth(280)
            btn.setFixedHeight(100)
            btn.setStyleSheet("background-color : rgb(30,30,30);\n"
                    "color : white;\n"
                    "padding-left:60px;\n"
                    "border-radius: 8px;")
            self.videpListVbox.addWidget(btn)
        self.videoListWidget.setLayout(self.videpListVbox)
        self.videoScroll.setWidget(self.videoListWidget)

        #상단바 부분

        #중복코드 인가?
        self.idLabel = QtWidgets.QLabel(self.pageList[3])
        self.idLabel.setGeometry(QtCore.QRect(50, 20, 140, 20))
        self.idLabel.setStyleSheet(
                "color : white;"
                "font-size: 13pt;")
        self.idLabel.setText("님 환영합니다!")

        self.videoPageBtnList = []
        videoPageBackBtn = QtWidgets.QPushButton(self.pageList[3])
        videoPageBackBtn.setGeometry(QtCore.QRect(1450,20,113,32))
        videoPageBackBtn.setStyleSheet("background-color : rgb(80,80,80);\n"
                "border-radius: 4px;\n"
                "font-size: 13pt;\n"
                "color : white;")
        videoPageBackBtn.setText("< Back")
        self.videoPageBtnList.append(videoPageBackBtn)   

        videoAddBtn = QtWidgets.QPushButton(self.pageList[3])
        videoAddBtn.setGeometry(QtCore.QRect(1320,20,113,32))
        videoAddBtn.setStyleSheet("background-color : rgb(220,0,0);\n"
                "padding-left : 2px;\n"
                "font-size: 13pt;\n"
                "border-radius: 4px;\n"
                "color : white;")
        videoAddBtn.setText("+ Add Video")
        self.videoPageBtnList.append(videoAddBtn)


        #영상 하단바
        self.idLabel = QtWidgets.QLabel(self.pageList[3])
        self.idLabel.setGeometry(QtCore.QRect(40, 840, 850, 40))
        self.idLabel.setStyleSheet(
                "color : white;"
                "font-size: 25pt;")
        self.idLabel.setText("Vidoe Title")

        self.videoWidget = QtWidgets.QWidget(self.pageList[3])
        self.videoWidget.setGeometry(QtCore.QRect(10, 50, 1280, 720))
        self.videoWidget.setStyleSheet("background-color : rgb(80,80,80);")

        self.slider = QtWidgets.QSlider(Qt.Horizontal, self.pageList[3])
        self.slider.move(30, 30)
        self.slider.setRange(0, 100)
        self.slider.setSingleStep(1)
        self.slider.setGeometry(10, 785, 110, 40)

        self.videoControlBtnList = []
        imageList  = ("play.png","pause.png","stop.png")
        for i in range(0,3):
            controlBtn = QtWidgets.QPushButton(self.pageList[3])
            controlBtn.setGeometry(QtCore.QRect(570+ 50 * i, 785, 40, 40))
            self.videoControlBtnList.append(controlBtn)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(imageList[i]), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.videoControlBtnList[i].setIcon(icon)
            self.videoControlBtnList[i].setIconSize(QtCore.QSize(40, 40))
            
    

        
