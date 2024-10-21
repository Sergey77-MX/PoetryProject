import collections
import re

from src.reader_data_csv import reader_file_transaction_csv
from src.reader_data_excel import reader_file_transaction_excel
from src.utils import financial_transactions


json_file = financial_transactions("..//data/operations.json")
csv_file = reader_file_transaction_csv("..//data/transactions.csv")
excel_file = reader_file_transaction_excel("..//data/transactions_excel.xlsx")


def search_transactions(transactions: list[dict], search_string: str) -> list[dict]:
    """Функция, принимает список словарей с данными о банковских операциях и строку поиска, а возвращает
    список словарей, у которых в описании есть данная строка"""
    result = []
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    for transaction in transactions:
        desc = transaction.get("description", "")
        if type(desc) and type(desc) is not str:
            pass
        elif re.search(pattern, desc):
            result.append(transaction)
    return result

# if __name__ == "__main__":
#     print(search_transactions(json_file, 'Перевод со счета на счет'))


def count_transactions(transactions: list[dict], user_categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    descriptions = []
    category = []
    count = []
    for transaction in transactions:
        descriptions.append(transaction.get("description"))

    for cat in user_categories:
        cat.lower()
        category.append(cat)

        for description in descriptions:
            d = str(description)
            if cat.lower() == d.lower():
                count.append(cat)
    return dict(collections.Counter(count))


# if __name__ == "__main__":
#     print(count_transactions(json_file, ["Перевод организации", "открытие вклада", "Перевод со счета на счет"]))
