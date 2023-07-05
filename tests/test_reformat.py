from utils import reformat


def test_number_card():
    assert reformat.number_card("1596837868705199") == "1596 83** **** 5199"


def test_number_account():
    assert reformat.number_account('123456789') == '**6789'


def test_date_reformat():
    assert reformat.date_reformat("2019-08-26T10:50:58.294041") == "2019.08.26"


def test_transaction_details():
    assert reformat.transaction_details("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert reformat.transaction_details("Счет 41421565395219882431") == "Счет **2431"
    assert reformat.transaction_details("") == ""
