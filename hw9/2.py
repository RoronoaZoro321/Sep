import js
from pyscript import document
from pyodide.ffi import create_proxy
from abc import ABC, abstractmethod
from datetime import datetime
import random

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

def convertToUSD(amount):
    return amount / 30

def convertToTHB(amount):
    return amount * 30

class ContainerWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.widgets = []
        
    def addWidget(self, widget):
        self.widgets.append(widget)
        
    def drawWidget(self):
        for widget in self.widgets:
            widget.drawWidget()


class CurrencyConverterWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        
    def onClick(self, event):
        amount = float(self.input_text.value)
        if self.convert_to.value == "USD":
            converted_amount = convertToUSD(amount)
            js.alert(f"{amount} THB is equivalent to {converted_amount} USD")
        elif self.convert_to.value == "THB":
            converted_amount = convertToTHB(amount)
            js.alert(f"{amount} USD is equivalent to {converted_amount} THB")
        
    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "600px"
        self.element.appendChild(self.input_text)
        
        self.convert_to = document.createElement("select")
        self.convert_to.innerHTML = "<option value='USD'>USD</option><option value='THB'>THB</option>"
        self.element.appendChild(self.convert_to)
        
        self.button = document.createElement("button")
        self.button.textContent = "Convert"
        self.button.onclick = self.onClick
        self.element.appendChild(self.button)

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

class ColorfulAnimationWidget(AnimationWidget):
    def __init__(self, element_id):
        AnimationWidget.__init__(self, element_id)
        
    def on_random_color_click(self, event):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.image.style.backgroundColor = f"rgb({r}, {g}, {b})"
        
    def drawWidget(self):
        AnimationWidget.drawWidget(self)
        self.random_color_button = document.createElement("button")
        self.random_color_button.textContent = "random color"
        self.random_color_button.onclick = self.on_random_color_click
        self.element.appendChild(self.random_color_button)

if __name__ == "__main__":
    container = ContainerWidget("container")
    
    currency_converter_widget = CurrencyConverterWidget("container")
    animation_widget = AnimationWidget("container")
    colorful_animation_widget = ColorfulAnimationWidget("container")
    
    container.addWidget(currency_converter_widget)
    container.addWidget(animation_widget)
    container.addWidget(colorful_animation_widget)
    
    container.drawWidget()