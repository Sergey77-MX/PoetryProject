from unittest.mock import patch

from src.external_api import convert_to_rub


@patch('requests.get')
def test_currency_conversion(mock_get, trans_1):
    mock_get.return_value.json.return_value = {"success": True, "query":
                                               {"from": "USD", "to": "RUB", "amount": "8221.37"}, "info":
                                               {"timestamp": 1724671757, "rate": 91.475458},
                                               "date": "2024-08-26", "result": 752053.58}
    assert convert_to_rub(trans_1) == 752053.58


@patch('requests.get')
def test_currency_conversion_2(mock_get, trans_2):
    mock_get.return_value.json.return_value = {"success": True, "query":
                                               {"from": "EUR", "to": "RUB", "amount": "8221.37"}, "info":
                                               {"timestamp": 1724671757, "rate": 91.475458},
                                               "date": "2024-08-26", "result": 752053.58}
    assert convert_to_rub(trans_2) == 752053.58


@patch('requests.get')
def test_currency_conversion_3(trans_3):
    assert convert_to_rub(trans_3) == None
