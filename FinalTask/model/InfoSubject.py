
class InfoSubject(object):
    def __init__(self, category, product, cost, dateBuy):
        """Constructor"""
        self.category = category
        self.product = product
        self.cost = cost
        self.dateBuy = dateBuy
    def __str__(self):
        string = "Category: " + self.category + "\n"
        string += "Product: " + self.product + "\n"
        string += "Cost: " + self.cost + "\n"
        string += "Date Buy: " + self.dateBuy + "\n"
        return string
    def getTuple(self):
        return [self.category,  self.product,
                self.cost,  self.dateBuy]
