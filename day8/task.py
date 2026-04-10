# Дано

# records = [
# {"file": "report.pdf", "size": 120},
# {"file": "../secret.txt", "size": 50},
# {"file": "image.png", "size": 200},
# {"file": "/etc/passwd", "size": 10},
# {"file": "notes.txt", "size": 80}
# ]

# Требуется

# Оставить только безопасные имена файлов
# Исключить:
# пути с ..
# абсолютные пути
# Вернуть список имён файлов
# Ожидаемый результат:
# ["report.pdf", "image.png", "notes.txt"]
