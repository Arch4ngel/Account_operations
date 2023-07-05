import json
import reformat


def prev_ops():
    """Функция вызывает 5 последних операций из файла данных"""
    data_init = json.load(open('operations.json', encoding='utf8'))
    data = []
    for item in data_init:
        if item.get("state") == "EXECUTED":
            data.append(item)
    i = 0
    output = ''
    while i < 5:
        output += f"{reformat.date_reformat(data[i]['date'])} {data[i]['description']}\n"
        output += f"{reformat.transaction_details(data[i].get('from', ''))} -> " \
                  f"{reformat.transaction_details(data[i].get('to', ''))}"
        output += f"\n{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n\n"
        i += 1
    return output
