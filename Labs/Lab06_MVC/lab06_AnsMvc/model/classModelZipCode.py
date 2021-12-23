class classModelZipCode(object):
    """
    Класс который хранит данные приложения

    """

    def __init__(self):
        """Constructor"""
        self.zip_codes = None
        self.read_zip_all()

    def getZipCodes(self):
        return self.zip_codes


    def read_zip_all(self):
        """
        Читает файл, который содержит информация о почтовых индексах,
        городах и штатах из csv файла и генерирует массив zip_codes = []
        :return: возвращает список с индексами и городами
        """
        i = 0
        header = []
        self.zip_codes = []
        zip_data = []
        skip_line = False
        # http://notebook.gaslampmedia.com/wp-content/uploads/2013/08/zip_codes_states.csv
        for line in open('../zip_codes_states.csv').read().split("\n"):
            skip_line = False
            m = line.strip().replace('"', '').split(",")
            i += 1
            if i == 1:
                for val in m:
                    header.append(val)
            else:
                zip_data = []
                for idx in range(0, len(m)):
                    if m[idx] == '':
                        skip_line = True
                        break
                    if header[idx] == "latitude" or header[idx] == "longitude":
                        val = float(m[idx])
                    else:
                        val = m[idx]
                    zip_data.append(val)
                if not skip_line:
                    self.zip_codes.append(zip_data)
