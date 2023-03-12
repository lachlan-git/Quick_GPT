import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QComboBox, QTextEdit, QPushButton


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Create the user interface elements
        self.dropdown = QComboBox()
        self.dropdown.addItems(['Option 1', 'Option 2', 'Option 3'])
        self.button = QPushButton('Press me')
        self.button.clicked.connect(self.button_clicked)  # Connect the clicked signal to a slot
        self.textedit = QTextEdit()
        self.label = QLabel('This is a label')
        self.bottom_button_1 = QPushButton('Button 1')
        self.bottom_button_2 = QPushButton('Button 2')

        # Create a grid layout for the elements
        grid = QGridLayout()
        self.setLayout(grid)

        # Add the elements to the grid layout
        grid.addWidget(self.dropdown, 0, 0)
        grid.addWidget(self.button, 0, 1)
        grid.addWidget(self.textedit, 1, 0, 1, 2)
        grid.addWidget(self.label, 2, 0, 1, 2)
        grid.addWidget(self.bottom_button_1, 3, 0)
        grid.addWidget(self.bottom_button_2, 3, 1)

        # Set the window properties
        self.setWindowTitle('MyApp')
        self.setGeometry(100, 100, 400, 300)
        self.show()

    def button_clicked(self):
        print('Button clicked!')  # Replace with your desired function


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
