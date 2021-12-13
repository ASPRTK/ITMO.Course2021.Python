import json

filename = 'person.json'

info = {
    "ФИО": "Иванов Иван Петрович",
    "Рейтинг": {
        "Знания": 90,
        "Умения": 85,
        "Навыки": 80
    },
    "Возможности": ["Аккуратность", "Стрессоустойчивость"],
    "Возраст": 35.5,
    "Хобби": None
}

# Запись структуры в файл в JSON-формате
with open(filename, "w", encoding="utf-8") as fh:
    fh.write(json.dumps(info, ensure_ascii=False, indent=4))


# Чтение из файла JSON-формата
info_2 = []
with open(filename, encoding="utf-8") as fh:
    info_2 = json.loads(fh.read())

print(info_2)
