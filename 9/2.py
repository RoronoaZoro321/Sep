import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime

class AbstractWidget(ABC):
    def __init__(self, element_id):
        self.element_id = element_id
        self._element = None
        
    @property
    def element(self):
        if not self._element:
            self._element = document.querySelector(f"#{self.element_id}")
        return self._element
    
    @abstractmethod
    def drawWidget(self):
        pass

class AnimationWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.counter = 1
        self.pause = False
        
    def on_click(self, event):
        if self.button.textContent == "pause":
            self.button.textContent = "play"
            self.pause = True
        else:
            self.button.textContent = "pause"
            self.pause = False
            
    def on_setInterval(self):
        if not self.pause:
            self.counter += 1
            if self.counter > 20:
                self.jump_sound.play()
                self.counter = 1
            self.image.src = f"../4/images/frame-{self.counter}.png"
        
    def drawWidget(self):
        self.image = document.createElement("img")
        self.image.style.width = "600px"
        self.image.style.height = "600px"
        self.image.src = "../4/images/frame-1.png"
        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)
        self.element.appendChild(self.image)
        
        self.jump_sound = js.Audio.new("../4/sounds/rabbit_jump.wav")

        self.button = document.createElement("button")
        self.button.textContent = "pause"
        self.button.onclick = self.on_click
        self.element.appendChild(self.button)
        
if __name__ == "__main__":
    widget = AnimationWidget("container")
    widget.drawWidget()