def number_card(num):
    """Функция делает номер карты читаемым и скрыавет часть символов"""
    num_new = num[:4] + ' ' + num[4:6] + '**' + ' **** ' + num[-4:]
    return num_new


def number_account(num):
    """Функция скрывает полный номер счета"""
    num_new = '**' + num[-4:]
    return num_new


def date_reformat(date):
    """Функция делает дату операции читаемой"""
    date_new = date[:10].replace('-', '.')
    return date_new


def transaction_details(data):
    """Функция выбирает способ форматирования номера счета или карты"""
    new_data = ''
    if "Счет" in data:
        new_data = f"Счет {number_account(data)}"
    elif data == '':
        new_data = ''
    else:
        new_data = f"{data[:-16]}{number_card(data[-16:])}"
    return new_data
