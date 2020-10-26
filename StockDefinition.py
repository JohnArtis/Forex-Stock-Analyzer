class stock(object):
    def __init__(self, name, openPrice, closePrice, price):
        self.name = name
        self.openPrice = openPrice
        self.price = price
        self.closePrice = closePrice

    #method allow stock prices to be updated daily
    def update(self, openPrice, closePrice):
        self.openPrice = openPrice
        self.closePrice = closePrice

    def update(self, price):
        self.price = price

