

class InfoSubject(object):
    def __init__(self, categori, product, cost, dateBuy):
        """Constructor"""
        self.categori = categori
        self.product = product
        self.cost = cost
        self.dateBuy = dateBuy
    def __str__(self):
        string = "Categori: " + self.categori + "\n" \        
            "product: " + self.product + "\n" \ 
            "cost: " + self.cost + "\n" \ 
            "dateBuy: " + self.dateBuy + "\n"
        return string

