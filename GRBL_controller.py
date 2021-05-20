import sys

import serial

import time

from PyQt5 import QtWidgets, uic


class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()

        uic.loadUi('GRBL_Controller.ui', self)

        self.init_ui()

        self.show()
    def init_ui(self):

        # Directions
        self.pushButton_Up.clicked.connect(self.pushButton_up_clicked)
        self.pushButton_Down.clicked.connect(self.pushButton_down_clicked)
        self.pushButton_Right.clicked.connect(self.pushButton_right_clicked)
        self.pushButton_Left.clicked.connect(self.pushButton_left_clicked)
        self.pushButton_Up_Z.clicked.connect(self.pushButton_up_z_clicked)
        self.pushButton_Down_Z.clicked.connect(self.pushButton_down_z_clicked)

        self.serialPort = None

        self.stopGCode = False
        self.flagOK = False
        

        


    def pushButton_right_clicked(self,step):
        
        print("Button X+ clicked.")
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())
 
        gcode=(
"""G01 X"""+str(step)+""" F"""+str(feed)+"""
""")
        print(gcode)
        self.sendGCode(gcode)
        
    def pushButton_down_clicked(self,step):
        
        print("Button Y- clicked.")
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())

        gcode=(
"""G01 Y"""+str(step)+"-"+""" F"""+str(feed)+"""
""")
    
        self.sendGCode(gcode)

    def pushButton_up_clicked(self,step,):
        
        print("Button Y+ clicked.")
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())

        gcode=(
"""G01 Y"""+str(step)+""" F"""+str(feed)+"""
""")
    
        self.sendGCode(gcode)
        
    def pushButton_left_clicked(self,step):
        
        print("Button X- clicked.")
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())

        gcode=(
"""G01 X"""+str(step)+"-"+""" F"""+str(feed)+"""
""")
    
        self.sendGCode(gcode)

    def pushButton_up_z_clicked(self,step):
        
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())
        
        gcode=(
"""G01 Z"""+str(step)+""" F"""+str(feed)+"""
""")

        self.sendGCode(gcode)
        
    def pushButton_down_z_clicked(self,step):
        
        
        step = self.comboBox_Step_Size.currentText()
        feed = int(self.comboBox_Feed_Rate.currentText())
        
        gcode=(
"""G01 Z"""+str(step)+"-"+""" F"""+str(feed)+"""
""")

        self.sendGCode(gcode)
        
        
        
    
    def sendGCode(self,gcode):
        portname = self.comboBox_Port_Name.currentText()
        baudrate = self.comboBox_Baud_Rate.currentText()
        ser = serial.Serial(portname, baudrate, timeout=1)
        ser.close()
        ser.open()
        ser.write(gcode.encode())
        time.sleep(3)
        read_val = ser.read(size=64)
        print (read_val)
        ser.write(gcode.encode())
        read_val = ser.read(size=64)
        print (read_val)
        if (read_val == ''):
            print (portname)

app = QtWidgets.QApplication(sys.argv)

window = Ui()

app.exec_()
