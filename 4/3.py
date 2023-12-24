import sys
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import QSoundEffect
import random

class Rabbit:
    def __init__(self):
        self.image = QPixmap("4/images/rabbit.png")
        self.x = 0
        self.y = 0
        self.w = 40
        self.h = 40

    def draw(self,p):
        p.drawPixmap(QRect(self.x,self.y,self.w,self.h),self.image)

    def random_pos(self, arena_width, arena_height):
        self.x = random.randint(0,arena_width - self.w)
        self.y = random.randint(0,arena_height - self.h)

    def is_hit(self, mouse_x, mouse_y):
        return self.x <= mouse_x <= self.x + self.w and self.y <= mouse_y <= self.y + self.h


class Animation_area(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setMinimumSize(300,300)
        self.arena_w = 300
        self.arena_h = 300
        self.rabbit = Rabbit()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(500)
        
        self.QSH = QSoundEffect()
        self.QSH.setSource(QUrl.fromLocalFile("4/sounds/rabbit_hit.wav"))
        self.QSM = QSoundEffect()
        self.QSM.setSource(QUrl.fromLocalFile("4/sounds/rabbit_missed.wav"))        

    def mousePressEvent(self, e):
        if self.rabbit.is_hit(e.pos().x(), e.pos().y()):
            # self.rabbit.random_pos(self.arena_w, self.arena_h)
            self.QSH.play()
            print("Hit!")
        else:
            self.QSM.play()
            print("Missed!")        
        self.update()

    def paintEvent(self,e):
        p = QPainter()
        p.begin(self)
        self.rabbit.draw(p)
        p.end()      

    def update_value(self):
        self.rabbit.random_pos(self.arena_w, self.arena_h)
        self.update()

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.anim_area = Animation_area()
        layout = QVBoxLayout()
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
