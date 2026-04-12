# Дано

# files = [
#     "report.pdf",
#     "image.png",
#     "archive.zip",
#     "script.py",
#     "notes.txt",
#     "payload.pkl",
#     "backup.tar.gz",
#     "../file.pdf",
#     "/etc/passwd.pdf",
#     "  ",
#     "",
#     None
# ]

# Требуется

# оставить только файлы с разрешёнными расширениями:
# .pdf
# .png
# .txt
# вернуть новый список
# сравнение должно быть безопасным:
# учитывать регистр
# не пропускать опасные расширения вроде .pkl
