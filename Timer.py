import time

class Timer : 
    def __init__(self) :
        self.StartBrowsing = time.time()
        self.EndBrowsing = None

    def EndTimer(self) : 
        self.EndBrowsing = time.time()

    def GetDurationBrowsing(self) : 
        duration = self.EndBrowsing - self.StartBrowsing
        return duration