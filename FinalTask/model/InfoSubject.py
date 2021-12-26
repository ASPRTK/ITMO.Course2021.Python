
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
    def __formatT(self, text):
        string = text
        if len(text) < 4:
            string += "\t\t\t\t\t"
        elif len(text) < 8:
            string += "\t\t\t\t"
        elif len(text) < 12:
            string += "\t\t\t"
        elif len(text) < 16:
            string += "\t\t"
        elif len(text) < 20:
            string += "\t"
        return string

    def getStrTupleT(self):
        #string = self.category
        string = self.__formatT(self.category)
        string += self.__formatT(self.product)
        string += self.__formatT(self.cost)
        string += self.__formatT(self.dateBuy)
        return string

    def getTuple(self):
        return [self.category,  self.product,
                self.cost,  self.dateBuy]
