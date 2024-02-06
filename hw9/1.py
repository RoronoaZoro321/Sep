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

# class AnimationWidget(AbstractWidget):
#     def __init__(self, element_id):
#         AbstractWidget.__init__(self, element_id)
#         self.counter = 1
            
#     def on_setInterval(self):
#         if not self.pause:
#             self.counter += 1
#             if self.counter > 20:
#                 self.jump_sound.play()
#                 self.counter = 1
#             self.image.src = f"../4/images/frame-{self.counter}.png"

#     def drawWidget(self):
#         self.image = document.createElement("img")
#         self.image.style.width = "600px"
#         self.image.style.height = "600px"
#         self.image.src = "./images/medicine.png"
#         on_setInterval = create_proxy(self.on_setInterval)
#         js.setInterval(on_setInterval, 100)
#         self.element.appendChild(self.image)
        
#         self.jump_sound = js.Audio.new("../4/sounds/rabbit_jump.wav")

#         self.button = document.createElement("button")
#         self.button.textContent = "pause"
#         self.button.onclick = self.on_click
#         self.element.appendChild(self.button)

class Item:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")

class Medicine(Item):
    def __init__(self, name, type, quantity):
        super().__init__(name, type)
        self.quantity = quantity
    
    def display_details(self):
        super().display_details()
        print(f"Quantity: {self.quantity}")

class Tool(Item):
    def __init__(self, name, type, available):
        super().__init__(name, type)
        self.available = available
    
    def display_details(self):
        super().display_details()
        print(f"Available: {self.available}")

class SearchWidget(AbstractWidget):
    def __init__(self, element_id):
        AbstractWidget.__init__(self, element_id)
        self.items = []
        self.counter = 10

    def add_item(self, item):
        self.items.append(item)

    def on_input_change(self, event):
        search_query = self.input_text.value.lower()
        self.clear_results()

        for item in self.items:
            if search_query in item.name.lower():
                self.display_result(item)

    def clear_results(self):
        while self.results.firstChild:
            self.results.removeChild(self.results.firstChild)

    def display_result(self, item):
        result_div = document.createElement("div")
        result_div.style.animation = "shake 0.5s infinite"
        result_div.style.marginBottom = "10px"

        name_span = document.createElement("span")
        name_span.textContent = f" Name: {item.name}"
        result_div.appendChild(name_span)

        type_span = document.createElement("span")
        type_span.textContent = f" Type: {item.type}"
        result_div.appendChild(type_span)

        if isinstance(item, Medicine):
            quantity_span = document.createElement("span")
            quantity_span.textContent = f" Quantity: {item.quantity}"
            result_div.appendChild(quantity_span)

        if isinstance(item, Tool):
            available_span = document.createElement("span")
            available_span.textContent = f" Available: {item.available}"
            result_div.appendChild(available_span)

        self.results.appendChild(result_div)

    def on_setInterval(self):
        self.counter += 10
        self.image.style.transform = f"rotate({self.counter}deg)"

    def on_click(self, event):
        self.jump_sound.play()

    def drawWidget(self):
        self.input_text = document.createElement("input", type="text")
        self.input_text.style.width = "60px"
        self.input_text.oninput = self.on_input_change
        self.element.appendChild(self.input_text)

        self.results = document.createElement("div")
        self.element.appendChild(self.results)

        on_setInterval = create_proxy(self.on_setInterval)
        js.setInterval(on_setInterval, 100)

        self.jump_sound = js.Audio.new("./sounds/rabbit_jump.wav")
        self.element.appendChild(self.jump_sound)

        self.image = document.createElement("img")
        self.image.style.width = "60px"
        self.image.style.height = "60px"
        self.image.src = "./images/medicine.png"
        self.image.onclick = self.on_click
        self.element.appendChild(self.image)

        self.p = document.createElement("p")
        self.p.textContent = "click on image to play sound"
        self.element.appendChild(self.p)

if __name__ == "__main__":
    widget = SearchWidget("search-container")
    widget.add_item(Medicine("Medicine Autex", "Type A", 10))
    widget.add_item(Medicine("Medicine Bubell", "Type B", 5))
    widget.add_item(Tool("Tool Aakey", "Type A", False))
    widget.add_item(Tool("Tool Buelly", "Type B", True))
    widget.drawWidget()