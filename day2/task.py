# Дано:

# CLI:
# python app.py --email test@test.com --password 123

# Сделать:

# проверить валидность email/password
# вывести ошибку если невалидно

# Использовать:

# argparse, другие библиотеки по желанию


import sys
import argparse
import re

sys.argv = ['app.py', '--email', 'test@test.com', '--password', 'qwerty123']

def validate_email(email):
    if not email or not re.match(r'^\S+@\S+\.\S+$', email):
        print("Incorrect e-mail!")
        return False

    domain = email.split('@')[1]
    tld = domain.split('.')[-1]

    if len(tld) < 2:
        print("Incorrect e-mail!")
        return False
    
    return True

def validate_password(password):
    if not password:
        print("ну я так не играю...")
        return False

    if re.search(r'qwerty123', password, re.IGNORECASE):
        print("ну за дурака меня не держи")
        return False
        
    if len(password) < 8:
        print("маловато будет...")
        return False

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        print("эти символы можно получить зажав кнопку shift")
        return False

    if password.isdigit():
        print("это не пароль от кодового замка - нуно что-то посерьезнее!")
        return False

    if not re.search(r'[A-Z]', password):
        print("Need HIGH letter")
        return False

    if not re.search(r'[0-9]', password):
        print("Цифры Мейсон - цифры!")
        return False

    return True

parser = argparse.ArgumentParser()
parser.add_argument('--email', required=True)
parser.add_argument('--password', required=True)
args = parser.parse_args()

validate_email(args.email)
validate_password(args.password)
