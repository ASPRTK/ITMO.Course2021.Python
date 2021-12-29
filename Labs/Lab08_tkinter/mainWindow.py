from tkinter import *
from tkinter.ttk import Combobox
import webbrowser
import json

class mainWindow(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Airport Locator")
        self.window.geometry('500x250')

        self.countries = {}
        self.geo = {}
        self.openJsonFile()

        self.combo_country = Combobox(self.window)
        self.combo_country['values'] = tuple(sorted(self.countries.keys()))
        self.combo_country.current(0)  # установите вариант по умолчанию
        self.combo_country.grid(column=0, row=0)
        self.combo_country.bind("<<ComboboxSelected>>", self.country_selected)

        self.combo_city = Combobox(self.window)
        self.combo_city['values'] = tuple(sorted(self.countries[self.combo_country.get()]))
        self.combo_city.current(0)  # установите вариант по умолчанию
        self.combo_city.grid(column=1, row=0)

        btn = Button(self.window, text="Open in Google Maps", bg="black", fg="red", font=("Arial Bold", 10),
                     command= lambda: self.clicked_Button())
        btn.grid(column=2, row=0)

        self.window.mainloop()

    def clicked_Button(self):
        latitude = str(self.geo[self.combo_city.get()]['latitude'])
        longitude = str(self.geo[self.combo_city.get()]['longitude'])
        webbrowser.open('http://www.google.com/maps/@?api=1&map_action=map&center=' +
                        latitude + ',' + longitude + '&basemap=satellite', new=2)

    def country_selected(self, event):
        self.combo_city['values'] =  tuple(sorted(self.countries[self.combo_country.get()]))
        self.combo_city.current(0)

    def openJsonFile(self):
        with open('airports.json', 'r') as f_obj:
            airports = json.load(f_obj)
            for elem in airports:
                if elem['country'] not in self.countries:
                    self.countries[elem['country']] = []
                airport = elem['city']
                if elem['iata'] is not None and elem['iata'] != '\\N':
                    airport += '-' + elem['iata']
                elif elem['icao'] is not None and elem['icao'] != '\\N':
                    airport += '-' + elem['icao']
                self.countries[elem['country']].append(airport)
                self.geo[airport] = {'latitude': elem['latitude'], 'longitude': elem['longitude']}



