import json
import reformat


def prev_ops():
    data = json.load(open('operations.json', encoding='utf8'))
    i = 0
    output = ''
    while i < 5:
        if data[i]['state'] == 'EXECUTED':
            output += f"{reformat.date_reformat(data[i]['date'])} {data[i]['description']}\n"
            output += f"{reformat.transaction_details(data[i].get('from', ''))} -> " \
                      f"{reformat.transaction_details(data[i].get('to', ''))}"
            output += f"\n{data[i]['operationAmount']['amount']} {data[i]['operationAmount']['currency']['name']}\n\n"
            i += 1
    return output
