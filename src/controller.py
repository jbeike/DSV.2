# -*- coding: utf-8 -*-
"""
Created on Sun Jan 05 12:46:59 2014

@author: Acer
"""
from Filterentwurfsverfahren import *
from MainWindow import MainWindow
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import SIGNAL
import sys

class controller():
    def __init__(self):
        
        self.initUI()
        
    def initUI(self): 
        self.mw=MainWindow(self)
        self.mw.show()
        self.add_Filtermethods()
        #self.need_Param()
    def need_Param(self,a="HP",b="Chebychev 1",c="man"):
        if a=="HP" and b=="Chebychev 1": 
            b="cheby1"
            return self.filter.get(b).needHP()
        else:
            return "noch nicht implementiert"
    def add_Filtermethods(self):
        self.filter={}
        fobj=open("init.txt","r")
        for line in fobj:
            line=line.strip()
            #a=  eval(line) 
            a=getattr(sys.modules[__name__], line)()
            self.filter.update({line:a})
        fobj.close
  
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    c=controller()
    app.exec_()

    
    
if __name__ == '__main__':
    main() 