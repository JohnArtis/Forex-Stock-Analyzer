class userSettings(object):
    def __init__(self):
        self.rHeight = 1600
        self.rWidth = 1200

    def getHeight(self):
        
        return self.rHeight

    def getWidth(self):
        return self.rWidth
    
    def setHeight(self, x):
        self.rHeight = x
    def setWidth(self, x):
        self.rWidth = x
