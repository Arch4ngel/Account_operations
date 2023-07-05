def number_card(num):
    num_new = num[:4] + ' ' + num[4:6] + '**' + ' **** ' + num[-4:]
    return num_new


def number_account(num):
    num_new = '**' + num[-4:]
    return num_new


def date_reformat(date):
    date_new = date[:10].replace('-', '.')
    return date_new


def transaction_details(data):
    new_data = ''
    if "Счет" in data:
        new_data = f"Счет {number_account(data)}"
    elif data == '':
        new_data = ''
    else:
        new_data = f"{data[:-16]}{number_card(data[-16:])}"
    return new_data
