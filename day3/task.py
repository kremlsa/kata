# Дано:

# любой код выбрасывающий исключение, например деление на 0

# Сделать:

# Обернуть код в try/except
# Логировать ошибки

# Использовать:

# import logging

import logging
import getpass

username = getpass.getuser()

logging.basicConfig(
    level=logging.ERROR,
    format=f'%(asctime)s - {username} - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

try:
    result = 1 / 0
except ZeroDivisionError as e:
    logging.error(f"Зафиксировано деление на ноль!: {e}")
