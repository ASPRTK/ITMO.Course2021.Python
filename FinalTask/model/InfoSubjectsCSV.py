import csv
import os

from FinalTask.model.InfoSubject import InfoSubject


class InfoSubjectsCSV(object):
    def __init__(self):
        """Constructor"""
        self.__FILENAME = "InfoSubjects.csv"
        self.infoSubjects = list()
        self.checkingFile()

    def writeCSV(self):
        with open(self.__FILENAME, "a", newline="") as file:
            user = InfoSubject
            writer = csv.writer(file)
            writer.writerow(user)

    def add(self, infoSubject):
        with open(self.__FILENAME, "a", newline="") as file:
            user = infoSubject
            writer = csv.writer(file)
            writer.writerow(user)
        self.infoSubjects.add(infoSubject)

    def readCSV(self):
        with open(self.__FILENAME, "r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                infoSubject = InfoSubject(row[0], row[1], row[2], row[3])
                self.infoSubjects.add(infoSubject)

    def checkingFile(self):
        if os.path.exists(self.__FILENAME):
            self.readCSV()
        else:
            print("Файл не существует")









