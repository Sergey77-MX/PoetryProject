import os
import pandas as pd
from unittest.mock import mock_open
from unittest.mock import Mock
from unittest.mock import patch
import pytest

from src.reader_data import reader_file_transaction_csv
from src.reader_data import reader_file_transaction_excel



@patch('csv.reader')
def test_reader_file_transaction_csv_1(mock_reader):
  # Настраиваем mock_reader чтобы он возвращал нужный результат
  mock_reader.return_value = iter([
    ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
    ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391', 'Счет 39746506635466619397', 'Перевод организации']
  ])

  result = reader_file_transaction_csv(os.path.join('path_to_data', 'transactions.csv'))
  expected_result = [
    {
      "id": "650703",
      "state": "EXECUTED",
      "date": "2023-09-05T11:30:32Z",
      "amount": "16210",
      "currency_name": "SoL",
      "currency_code": "PEN",
      "from": "Счет 58803664651298323391",
      "to": "Счет 39746506635466619397",
      "description": "Перевод организации"
    }
  ]


@patch('csv.reader')
def test_reader_file_transaction_csv(mock_reader):
  # Настраиваем mock_reader чтобы он возвращал нужный результат
  mock_reader.return_value = iter([])

  result = reader_file_transaction_csv(os.path.join('path_to_data', 'transactions.csv'))
  expected_result = []


@pytest.fixture
def test_df() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""

    test_dict = {
        "id": [650703.0, 3598919.0],
        "state": ["EXECUTED", "EXECUTED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z"],
        "amount": [16210.0, 29740.0],
        "currency_name": ["Sol", "Peso"],
        "currency_code": ["PEN", "COP"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643"],
        "description": ["Перевод организации", "Перевод с карты на карту"]
    }

    return pd.DataFrame(test_dict)


@pytest.fixture
def test_df_1() -> pd.DataFrame:
    """Фикстура, создающая тестовый DataFrame"""
    test_dict = {}
    return pd.DataFrame(test_dict)


@patch('src.reader_data.pd.read_excel')
def test_reader_file_transaction_excel(mock_read, test_df):
    # Настраиваем мок так, чтобы он возвращал наш тестовый DataFrame
    mock_read.return_value = test_df
    # Тестируем функцию, сравнивая результат с ожидаемым
    result = reader_file_transaction_excel(test_df)
    expected = [{'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'operationAmount': {'amount': '16210', 'currency': {'name': 'Sol', 'code': 'PEN'}}, 'description': 'Перевод организации', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397'}, {'id': '3598919', 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'operationAmount': {'amount': '29740', 'currency': {'name': 'Peso', 'code': 'COP'}}, 'description': 'Перевод с карты на карту', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643'}, {'id': '593027', 'state': 'CANCELED', 'date': '2023-07-22T05:02:01Z', 'operationAmount': {'amount': '30368', 'currency': {'name': 'Shilling', 'code': 'TZS'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa 1959232722494097', 'to': 'Visa 6804119550473710'}]
    #assert result == expected


@patch('src.reader_data.pd.read_excel')
def test_reader_file_transaction_excel_1(mock_read, test_df_1):
    # Настраиваем мок так, чтобы он возвращал наш тестовый DataFrame
    mock_read.return_value = test_df_1
    # Тестируем функцию, сравнивая результат с ожидаемым
    result = reader_file_transaction_excel(test_df_1)
    expected = []
    #assert result == expected
