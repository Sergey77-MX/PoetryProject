import csv

from pathlib import Path

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "transactions.csv"


def reader_file_transaction_csv(path):
    """Принимает путь до CSV-файла и возвращает список словарей с данными о финансовых транзакциях."""
    transaction_list = []
    try:
        with open(path, "r", encoding="utf-8") as transactions:
            reader = csv.reader(transactions, delimiter=';')
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
#     print(reader_file_transaction_csv('/home/sergey/Рабочий стол/мои проекты/PoetryProject/data/transactions.csv'))