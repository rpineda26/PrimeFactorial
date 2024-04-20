from PyQt5.QtWidgets import QApplication
import sys
from view import *

"""
Author : Ralph Dawson G. Pineda
About: Technical Assessment for the position of Software Engineer Intern: 
Date : April 2024
Primality Test and Factorial Computation

"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    machine = Machine()
    machine.showMaximized()
    sys.exit(app.exec_())