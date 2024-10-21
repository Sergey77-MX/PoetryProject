from unittest.mock import patch


@patch('csv.reader')
def test_reader_file_transaction_csv_1(mock_reader):
    mock_reader.return_value = iter([
        ['id', 'state', 'date', 'amount', 'currency_name', 'currency_code', 'from', 'to', 'description'],
        ['650703', 'EXECUTED', '2023-09-05T11:30:32Z', '16210', 'SoL', 'PEN', 'Счет 58803664651298323391',
         'Счет 39746506635466619397', 'Перевод организации']
    ])


@patch('csv.reader')
def test_reader_file_transaction_csv(mock_reader):
    mock_reader.return_value = iter([
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
      ])


@patch('csv.reader')
def test_reader_file_transaction_csv_2(mock_reader):
    mock_reader.return_value = iter([])


@patch('src.reader_data_excel.pd.read_excel')
def test_reader_file_transaction_excel(mock_read, test_df):
    mock_read.return_value = test_df


@patch('src.reader_data_excel.pd.read_excel')
def test_reader_file_transaction_excel_1(mock_read, test_df_1):
    mock_read.return_value = test_df_1


@patch('src.reader_data_excel.pd.read_excel')
def test_reader_file_transaction_excel_2(mock_read, test_df_2):
    mock_read.return_value = test_df_2
