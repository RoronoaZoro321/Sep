class Time:
    def __init__(self, hour, min, sec):
        self.hour = hour
        self.min = min
        self.sec = sec
    
    def getHour(self):
        return self.hour
    def getMin(self):
        return self.min
    def getSec(self):
        return self.sec
    
    def setHour(self, hour):
        self.hour = hour
    def setMin(self, min):
        self.min = min
    def setSec(self, sec):
        self.sec = sec
    
    def print(self):
        print(f"{self.hour:02d}:{self.min:02d}:{self.sec:02d} Hrs")
        
time1 = Time(9, 30, 0)
time1.print()