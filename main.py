from PyQt5.QtWidgets import QApplication
import sys
from view import *

"""
Author : Ralph Dawson G. Pineda
About: Technical Assessment for the position of Software Engineer Intern: 
Date : April 2024
Primality Test and Factorial Computation
Todo checklist:     

    - [x] 1. Implement GUI for accepting input and displaying output
    - [x] 2. Implement primality test
    - [x] 3. Implement factorial computation
    - [x] 4. Documentation
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = View()
    view.showNormal()
    sys.exit(app.exec_())