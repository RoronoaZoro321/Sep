import sys
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class Animal:
    def __init__(self, image_path):
        self.image = QPixmap(image_path)
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40
        self.vy = 1
        self.sound = QSoundEffect()

    def draw(self, p):
        p.drawPixmap(QRect(self.x, self.y, self.w, self.h), self.image)

    def random_pos(self, arena_width):
        self.x = random.randint(0, arena_width - self.w)
        self.y = 0

    def is_hit(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h

    def update_position(self, arena_height):
        self.y += self.vy
        if self.y > arena_height:
            self.random_pos(arena_height)

class Dog(Animal):
    def __init__(self):
        super().__init__("4/hw/images/dog.png")
        self.sound.setSource(QUrl.fromLocalFile("4/hw/sounds/dog.wav"))

class Cat(Animal):
    def __init__(self):
        super().__init__("4/hw/images/cat.png")
        self.sound.setSource(QUrl.fromLocalFile("4/hw/sounds/cat.wav"))

class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setMinimumSize(300,300)
        self.arena_w = 300
        self.arena_h = 300
        self.cat = Cat()
        self.dog = Dog()
        self.cat.random_pos(self.arena_w)
        self.dog.random_pos(self.arena_w)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(4)  # Adjust the timer interval to control the falling speed

    def update_value(self):
        self.cat.update_position(self.arena_h)
        self.dog.update_position(self.arena_h)
        self.update()

    def mousePressEvent(self, e):
        if self.cat.is_hit(e.pos().x(), e.pos().y()):
            self.cat.sound.play()
            self.cat.random_pos(self.arena_w)
        elif self.dog.is_hit(e.pos().x(), e.pos().y()):
            self.dog.sound.play()
            self.dog.random_pos(self.arena_w)

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        self.cat.draw(p)
        self.dog.draw(p)
        p.end()

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.anim_area = Animation_area()
        layout = QVBoxLayout()
        
        label = QLabel("Click on the Cat not Dog!!")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("font-size: 20px; font-weight: bold; color: red;")
        
        layout.addWidget(label)
        layout.addWidget(self.anim_area)
        
        self.setLayout(layout)
        self.setMinimumSize(330,400)
    
def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
