class stock(object):
    def __init__(self, name, openPrice, closePrice):
        self.name = name
        self.openPrice = openPrice
        self.closePrice = closePrice

    #method allow stock prices to be updated daily
    def update(self, openPrice, closePrice):
        self.openPrice = openPrice
        self.closePrice = closePrice


