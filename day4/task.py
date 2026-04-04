# прочитать файл access.log
# найти строки с ERROR

import logging
import getpass
import traceback

username = getpass.getuser()

logging.basicConfig(
    level=logging.ERROR,
    format=f'%(asctime)s - {username} - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='errors.log',
    encoding='utf-8'
)

try:
    result = 1 / 0
except ZeroDivisionError as e:
    logging.error("Зафиксировано деление на ноль!", exc_info=True)

with open('errors.log', 'r', encoding='utf-8') as file:
    for line in file:
        if 'ERROR' in line:
            print(line.strip())

#добавил к прошлому коду логгирование stacktrace
#без utf8 что-то не получалось по дефолту считать данные из лог файла (вместо данных были коды ascii)
