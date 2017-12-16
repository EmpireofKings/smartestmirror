#!/usr/bin/python
'''
author: Tobias Weis
'''
import cv2
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
import calendar
import numpy as np
from widgets.Base import *
import time

class Webcam(QLabel,Base):
    """
    Get webcam images, process and display them
    """
    def __init__(self, title, parent, serviceRunner):
        super(Webcam,self).__init__(title,parent)
        self.parent = parent
        self.config = None
        self.capture = cv2.VideoCapture(0)

    def setimg(self,img):
        img = np.require(img, np.uint8, 'C')
        qimg = QImage(img.data, img.shape[1], img.shape[0], img.strides[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)
        self.setPixmap(pixmap)

    def update(self):
        # create a pretty timestring
        #img = np.zeros((100,200,3), np.uint8) + [255,255,255]
        ret,img = self.capture.read()
        if img is not None:
            #img = cv2.imread("brain.jpg")
            self.setimg(img)
        else:
            print("None")
