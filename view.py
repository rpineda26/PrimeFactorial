"""
Author: Ralph Dawson G. Pineda
Date: April 2024
Description: This file contains the view of the program. Make sure that the dependencies are installed in your device. Read the README.md for more information.
"""
from PyQt5.QtWidgets import QMessageBox, QLabel, QFileDialog, QWidget, QGridLayout, QPushButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QInputDialog, QLineEdit
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont, QIntValidator
from PyQt5.QtCore import Qt

from controller import *

"""
@definition : This class is the view representation of the entire machine. The flow of user input is: (open text file -> (input word -> start -> step *)*)*) where * means repetition
@attributes: machine - the DFA that is being represented by the view
"""

class Machine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Technical Assessment for Internship')
        self.setFixedWidth(720)
        self.setFixedHeight(720)

        self.vbox = QVBoxLayout()
        
        self.vbox.setAlignment(Qt.AlignTop)
        self.setLayout(self.vbox)
        self.displayInputBtns()
        self.displayPrimeResults()
        self.dispplayFactorialResults()

    
    """
    @definition: This function creates a horizontal layout to display the input buttons
    """
    def displayInputBtns(self):
        hbox = QHBoxLayout()
        self.startButton = QPushButton('Start')
        self.inputNumberLabel = QLabel('Input Non-negative Integer:')
        self.inputNumber = QLineEdit()
        self.inputNumber.setValidator(QIntValidator())

        hbox.addWidget(self.inputNumberLabel)
        hbox.addWidget(self.inputNumber)
        hbox.addWidget(self.startButton)
        

        self.startButton.clicked.connect(self.startCalculate)
        self.inputNumber.textChanged.connect(self.enableStartButton)
        self.inputNumber.returnPressed.connect(self.startCalculate)

        self.startButton.setEnabled(False)
        self.vbox.addLayout(hbox)
    """
    @definition: This function creates a horizontal layout to display the status bar
    """

    def displayPrimeResults(self):
        self.prime_result_label = QLabel("Is Prime: ")
        primeBox = QVBoxLayout()
        primeBox.addWidget(self.prime_result_label)
        self.vbox.addLayout(primeBox)
    def dispplayFactorialResults(self):
        self.factorial_product_label = QLabel("Product: ")
        factorialBox = QVBoxLayout()
        factorialBox.addWidget(self.factorial_product_label)
        self.vbox.addLayout(factorialBox)
 
    """
    @definition: This function enables the start button when the user inputs a non negative number. The start button will not start
                 when the input is empty, negative, or not a number.
    """
    def enableStartButton(self):
        if self.inputNumber.text() != "" and self.inputNumber.text().isnumeric():
            self.startButton.setEnabled(True)
        else:
            self.startButton.setEnabled(False)
    """
    @definition: This function is called when the user clicks the start button. It will
                    initialize the values needed to start tracing the transition of states
    """
    def startCalculate(self):
        """
        Start the path finding algorithm
        """
        if self.startButton.isEnabled():
            primeFlag = isPrime(int(self.inputNumber.text()))
            factorialProduct = factorial(int(self.inputNumber.text()))
            self.prime_result_label.setText("Is Prime: "+str(primeFlag))
            self.factorial_product_label.setText("Product: "+str(factorialProduct))
        else:
            self.showEndMessage()
 
    """
    @definition: This function shows the message when the machine terminates. 
                 It will display whether the word was accepted or rejected
    """
    def showEndMessage(self):
        message = QMessageBox()
        title = "Error"
        msg = "Make sure to input a non-negative integer!"
        message.setIcon(QMessageBox.Information)
        
        message.setWindowTitle(title)
        message.setText(msg)
        message.setStandardButtons(QMessageBox.Ok)

        message.exec_()
        
