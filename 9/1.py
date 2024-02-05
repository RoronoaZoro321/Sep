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

def convertToUSD(amount):
    return amount / 30

def convertToTHB(amount):
    return amount * 30

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
        
if __name__ == "__main__":
    widget = CurrencyConverterWidget("container")
    widget.drawWidget()