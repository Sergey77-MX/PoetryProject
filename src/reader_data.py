import csv

import pandas as pd


transactions = '/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions.csv'
def reader_file_transaction_csv(transactions):
    """Function get data from csv file."""
    transaction_list = []
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



# if __name__ == "__main__":
#     result = reader_file_transaction_csv('/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions.csv')
#     print(result)


def reader_file_transaction_excel(transactions_xlsx):
    """Функция считывающая файл в формате excel и возвращающая список словарей"""
    transaction_xlsx_list = []
    transactions_xlsx = pd.read_excel("/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions_excel_1.xlsx")
    #print(transactions_xlsx)
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
    return transaction_xlsx_list



# if __name__ == "__main__":
#     result = reader_file_transaction_excel("/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions_excel_1.xlsx")
#     print(result)


# print(reader_file_transaction_csv("/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions.csv"))
# print(reader_file_transaction_excel("/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions_excel_1.xlsx"))
