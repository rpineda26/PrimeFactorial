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
class View(QWidget):
    def __init__(self):
        super().__init__()
        #initialize the window
        self.setWindowTitle('Technical Assessment for Internship')
        self.setFixedWidth(720)
        self.setFixedHeight(360)

        #initialize the main vertical layout
        self.vbox = QVBoxLayout()   
        self.vbox.setAlignment(Qt.AlignTop)
        self.setLayout(self.vbox)

        #add the visual elements (input buttons, prime result, factorial result) to the layout
        self.displayInputBtns()
        self.displayPrimeResults()
        self.dispplayFactorialResults()

    """
    @definition: This function creates a horizontal layout to display the input gui elements
                This includes: input number label, input number text field, and start button
    """
    def displayInputBtns(self):

        #initialize the horizontal layout and input buttons
        hbox = QHBoxLayout()
        self.startButton = QPushButton('Start')
        self.inputNumberLabel = QLabel('Input Non-negative Integer:')
        self.inputNumber = QLineEdit()
        #only accept integer inputs, this doesnt prevent negative inputs
        self.inputNumber.setValidator(QIntValidator()) 

        #add the input buttons to the horizontal layout
        hbox.addWidget(self.inputNumberLabel)
        hbox.addWidget(self.inputNumber)
        hbox.addWidget(self.startButton)

        #add event listeners for the input buttons
        self.startButton.clicked.connect(self.startCalculate)
        self.inputNumber.textChanged.connect(self.enableStartButton)
        self.inputNumber.returnPressed.connect(self.startCalculate)

        #initialize the startButton as disabled
        self.startButton.setEnabled(False)
        self.vbox.addLayout(hbox)
    """
    @definition: This function creates a horizontal layout to display the prime result gui elements
                This includes: prime result label, prime result text field
    """
    def displayPrimeResults(self):
        #initialize the horizontal layout and prime result gui elements
        primeHBox = QHBoxLayout()
        self.prime_result_label = QLabel("Is Prime: ")
        self.prime_result_data = QLineEdit()
        self.prime_result_data.setReadOnly(True)
        self.prime_result_data.setStyleSheet("background-color: white")
        primeHBox.addWidget(self.prime_result_label)
        primeHBox.addWidget(self.prime_result_data)
        #add the prime widgets to the vertical layout
        self.vbox.addLayout(primeHBox)
    """
    @definition: This function creates a horizontal layout to display the factorial result gui elements
                This includes: factorial result label, factorial result text field
    """
    def dispplayFactorialResults(self):
        #initialize the horizontal layout and factorial result gui elements
        factorialHBoxLayout = QHBoxLayout()
        self.factorial_product_label = QLabel("Product: ")
        self.factorial_product_data = QTextEdit()
        self.factorial_product_data.setReadOnly(True)
        self.factorial_product_data.setStyleSheet("background-color: white")
        factorialHBoxLayout.addWidget(self.factorial_product_label)
        factorialHBoxLayout.addWidget(self.factorial_product_data)
        #add the factorial widgets to the vertical layout
        self.vbox.addLayout(factorialHBoxLayout)
 
    """
    @definition: This function enables the start button when the user inputs a non negative number. The start button will not start
                 when the input is empty, negative, or not a number.
    """
    def enableStartButton(self):
        #reset colors of the label to display that results shown below are not based on the current input
        self.factorial_product_label.setStyleSheet("color: black")
        self.prime_result_label.setStyleSheet("color: black")
        self.prime_result_data.setStyleSheet("color: black")

        #enable the start button when the input is a non-negative integer
        if self.inputNumber.text() != "" and self.inputNumber.text().isnumeric():
            self.startButton.setEnabled(True)
        else:
            self.startButton.setEnabled(False)
    """
    @definition: This function is called when the user clicks the start button. It will
                    call the primality test and factorial computation functions from the controller.
                    Then, it will display the results in the GUI.
            
    """
    def startCalculate(self):
        """
        the app can call startCalculate even when the start button is disabled
        when the user utilizes the enter key instead of clicking the start button
         so we need to check if the start button is enabled
        """
        if self.startButton.isEnabled():
            #call the methods for primality test and factorial computation from the controller
            primeResult = optimized_isPrime_deterministic(int(self.inputNumber.text()))
            factorialResult = optimized_factorial(max=int(self.inputNumber.text()))
            #update the GUI with the results
            self.prime_result_data.setText(str (primeResult))
            self.factorial_product_data.setText(str(factorialResult))

            #emphasize the boolean result based on the color
            if(primeResult):
                self.prime_result_data.setStyleSheet("color: green")
            else:  
                self.prime_result_data.setStyleSheet("color: red")

            #display a visual signal that the results are based on the current input
            self.prime_result_label.setStyleSheet("color: blue")
            self.factorial_product_label.setStyleSheet("color: blue")

            #disable the start button after the computation, to prevent re-computation
            self.startButton.setEnabled(False)
            
        #The else block will only be reached through the enter key
        #scenario one: the input is negative, then the error message will be shown
        #scenario two: After a successful computation, the user presses enter again without changing the input 
        else:
            #show an error message when the input is invalid (occurs when enter key is pressed with a negative input)
            if int(self.inputNumber.text()) < 0:
                self.showEndMessage()
            #nothing will happen when the user presses enter after a successful computation without changing the input
 
    """
    @definition: This function shows the error message when the user presses "Enter" after inputting a negative number. 
                 It will display a warning message to the user.
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
        
