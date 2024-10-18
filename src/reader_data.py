import csv

import pandas as pd


def reader_file_transaction_csv(transactions):
    """Принимает путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    transaction_list = []
    transactions = '/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions.csv'
    try:
        with open(transactions) as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)  # Пропускаем заголовок таблицы
            for row in reader:
                if row:
                    id_, state, date, amount, currency_name, currency_code, from_, to, description = row
                    transaction_list.append(
                        {
                            "id": str(id_),
                            "state": state,
                            "date": date,
                            "operationAmount": {
                                "amount": str(amount),
                                "currency": {"name": currency_name, "code": currency_code},
                            },
                            "description": description,
                            "from": from_,
                            "to": to,
                        }
                    )
    except Exception:
        return []
    return transaction_list


def reader_file_transaction_excel(transactions_xlsx):
    """Принимает путь до EXCEL-файла и возвращает список словарей с данными о финансовых транзакциях"""
    transaction_xlsx_list = []
    transactions_xlsx = pd.read_excel("/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/"
                                      "transactions_excel_1.xlsx")
    try:
        len_, b = transactions_xlsx.shape
        for i in range(len_):
            if transactions_xlsx["id"][i]:
                transaction_xlsx_list.append(
                    {
                        "id": str(transactions_xlsx["id"][i]),
                        "state": transactions_xlsx["state"][i],
                        "date": transactions_xlsx["date"][i],
                        "operationAmount": {
                            "amount": str(transactions_xlsx["amount"][i]),
                            "currency": {
                                "name": transactions_xlsx["currency_name"][i],
                                "code": transactions_xlsx["currency_code"][i],
                            },
                        },
                        "description": transactions_xlsx["description"][i],
                        "from": transactions_xlsx["from"][i],
                        "to": transactions_xlsx["to"][i],
                    }
                )
            else:
                return []
    except KeyError:
        return []
    return transaction_xlsx_list
