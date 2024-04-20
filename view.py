"""
Author: Ralph Dawson G. Pineda
Date: April 2024
Description: This file contains the view of the program. Make sure that the dependencies are installed in your device. Read the README.md for more information.
"""
from PyQt5.QtWidgets import QMessageBox, QLabel, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from controller import *

"""
@definition : This class represents the view of the program. It is responsible for displaying the GUI of the program.

            Overall Structure: Vertical Layout (vbox)
                                    Horizontal layout (Input buttons)
                                            QLabel (Input Number)
                                            QLineEdit (Input Number)
                                            QPushButton (Start)
                                    Horizontal layout (Prime Result)
                                            QLabel (Prime Result)
                                            QLineEdit (Prime Result)
                                    Horizontal layout (Factorial Result)
                                            QLabel (Factorial Result)
                                            QTextEdit (Factorial Result)                                       
"""

class Machine(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Technical Assessment for Internship')
        self.setFixedWidth(720)
        self.setFixedHeight(360)
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
        primeHBox = QHBoxLayout()
        self.prime_result_label = QLabel("Is Prime: ")
        self.prime_result_data = QLineEdit()
        self.prime_result_data.setReadOnly(True)
        primeHBox.addWidget(self.prime_result_label)
        primeHBox.addWidget(self.prime_result_data)

        self.vbox.addLayout(primeHBox)
    def dispplayFactorialResults(self):
        factorialHBoxLayout = QHBoxLayout()
        self.factorial_product_label = QLabel("Product: ")
        self.factorial_product_data = QTextEdit()
        self.factorial_product_data.setReadOnly(True)
        factorialHBoxLayout.addWidget(self.factorial_product_label)
        factorialHBoxLayout.addWidget(self.factorial_product_data)
        self.vbox.addLayout(factorialHBoxLayout)
 
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
            #call the methods for primality test and factorial computation from the controller
            #update the GUI with the results
            self.prime_result_data.setText(str(naive_isPrime(int(self.inputNumber.text()))))
            self.factorial_product_data.setText(str(naive_factorial(int(self.inputNumber.text()))))
            #disable the start button after the computation, to prevent re-computation
            self.startButton.setEnabled(False) 
        else:
            #show an error message when the input is invalid (occurs when enter key is pressed with a negative input)
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
        