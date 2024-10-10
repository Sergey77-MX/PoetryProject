import json
import os

from dotenv import load_dotenv
from src.external_api import convert_to_rub


load_dotenv()
api_key = os.getenv("API_KEY")


def financial_transactions(path):
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, "r", encoding="utf-8") as operations:
            try:
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data


def transaction_amount(transactions, transaction_id):
    """Принимает транзакцию и возвращает сумму в рублях, если операция не в рублях, конвертирует"""
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                rub_amount = transaction["operationAmount"]["amount"]
                return rub_amount
            else:
                transaction_convert = dict()
                transaction_convert["amount"] = transaction["operationAmount"]["amount"]
                transaction_convert["currency"] = transaction["operationAmount"]["currency"]["code"]
                # print(transaction_convert)
                rub_amount = round(convert_to_rub(transaction_convert), 2)
                return rub_amount
    else:
        return "Транзакция не найдена"


# if __name__ == "__main__":
    # transactions = financial_transactions("../data/operations.json")
    # print(transaction_amount(transactions, 207126257))
