import sys
import math
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QWidget

HEIGHT = 600
WIDTH = 900

def create_gradient_button(parent, text, geometry, border_size=(3, 3), gradient_colors=('#FF5D47', '#FF0099', '#0066FF'), radius=20, hover_color='#FF0099', hover=True):
    # Create the container widget
    container = QWidget(parent)
    container.setGeometry(int(geometry[0]), int(geometry[1]), int(geometry[2] + border_size[0] * 2), int(geometry[3] + border_size[1] * 2))
    gradient = f'qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 {gradient_colors[0]}, stop:0.5 {gradient_colors[1]}, stop:1 {gradient_colors[2]})'
    container.setStyleSheet(f"""
        QWidget {{
            background-color: {gradient};
            border-radius: {radius}px;
        }}
    """)

    # Create the button
    button = QPushButton(text, container)
    button.setGeometry(border_size[0], border_size[1], geometry[2], geometry[3])
    
    if hover:
        button.setStyleSheet(f"""
        QPushButton {{
            background-color: #2A2B36;
            color: white;
            border-radius: {radius}px;
        }}
        QPushButton:hover {{
            background-color: {hover_color};  /* Change color on hover */
            color: #2A2B36;  /* Change text color on hover if needed */
        }}
        """)
    else:
        button.setStyleSheet(f"""
        QPushButton {{
            background-color: #2A2B36;
            color: white;
            border-radius: {radius}px;
        }}
        """)



    return container


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #2A2B36;")

        # Create a gradient button using the function

        background_outline = create_gradient_button(self, ' ', (math.floor(WIDTH)/2-200, math.floor(HEIGHT)/2-100 , 400, 200), radius=30, hover_color= "",hover=False)
        button1 = create_gradient_button(self, 'Open Identity', (math.floor(WIDTH/2)-150, math.floor(HEIGHT/2)-60, 300, 60))
        button2 = create_gradient_button(self, 'New Identity', (math.floor(WIDTH/2)-95, math.floor(HEIGHT/2)+10, 200, 60))

        self.setGeometry(300, 200, WIDTH, HEIGHT)
        self.setWindowTitle('Gradient Border Button')
        self.show()


def run():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
