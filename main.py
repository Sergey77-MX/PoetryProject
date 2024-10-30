import os

from _datetime import datetime

from src.widget import mask_account_card
from src.processing import filter_by_state, sort_by_date
from src.utils import PATH_TO_FILE, financial_transactions
from src.reader_data_csv import reader_file_transaction_csv, PATH_TO_CSV
from src.reader_data_excel import reader_file_transaction_excel, PATH_TO_EXCEL


def main():
    """Отвечает за основную логику проекта с пользователем и связывает функциональности между собой."""
    print("Добро пожаловать в программу работы с банковскими транзакциями.")
    print(
        """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    )

    transactions_from_file = []
    user_input_file = input()
    if user_input_file == "1":
        print("Для обработки выбран JSON-файл.")
        transactions_from_file = financial_transactions(os.path.abspath(PATH_TO_FILE))
    elif user_input_file == "2":
        print("Для обработки выбран CSV-файл.")
        transactions_from_file = reader_file_transaction_csv(PATH_TO_CSV)
    elif user_input_file == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions_from_file = reader_file_transaction_excel(PATH_TO_EXCEL)
    else:
        print("Введен некорректный номер.")
    print('Введите статус, по которому необходимо выполнить фильтрацию. '
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    user_state = input().upper()
    states_list = ['EXECUTED', 'CANCELED', 'PENDING']
    while user_state not in states_list:
        print(f"Статус операции {user_state} недоступен.")
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_state = input().upper()
    else:
        list_by_status = filter_by_state(transactions_from_file, user_state)
        print(f"Операции отфильтрованы по статусу {user_state}")
    print("Отсортировать операции по дате? Да/Нет")
    filter_transaction_date = []
    user_input_date = input().lower()
    if user_input_date == "да":
        print("Отсортировать по возрастанию или по убыванию? "
              "  по возрастанию/по убыванию")
        user_input = input().lower()
        if user_input == "по убыванию":
            filter_transaction_date = sort_by_date(list_by_status)
        elif user_input == "по возрастанию":
            direction = False
            filter_transaction_date = sort_by_date(list_by_status, direction)
        else:
            print("Введен некорректный ответ.")
    elif user_input_date == "нет":
        filter_transaction_date = list_by_status
    else:
        print("Введен некорректный ответ.")

    print("Выводить только рублевые транзакции?")
    user_input_curr = input("да/нет ").lower()
    rub_trans = []
    if user_input_curr == "да":
        for trans in filter_transaction_date:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                rub_trans.append(trans)
    elif user_input_curr == "нет":
        rub_trans = filter_transaction_date
    else:
        print("Введен некорректный ответ.")

    trans_word = []
    print("Отфильтровать список транзакций по определенному слову в описании?")
    sort_by_word = input("да/нет ").lower()
    if sort_by_word == "да":
        sort_by_word_yes = input("Введите слово для фильтрации: ")
        # trans_word = []
        for trans in rub_trans:
            if sort_by_word_yes in trans["description"]:
                trans_word.append(trans)
    elif sort_by_word == "нет":
        # trans_word = []
        for trans in rub_trans:
            trans_word.append(trans)
    else:
        print("Введен некорректный ответ.")
    if len(trans_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans_word)}\n")

    for trans in trans_word:
        if trans.get("from") and trans.get("to"):
            date = trans.get("date", "")[:19]
            bad_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            correct_date = bad_date.strftime("%d.%m.%Y")
            description = trans.get("description", "")
            masked_card_from = mask_account_card(str(trans.get("from")))
            masked_card_to = mask_account_card(str(trans.get("to")))
            masked_acc_from = mask_account_card(str(trans.get("from")))
            masked_acc_to = mask_account_card(str(trans.get("to")))
            amount = trans["operationAmount"]["amount"]
            if "Счет" in str(trans.get("from", "")) and "Счет" in str(trans.get("to", "")):
                print(f"{correct_date} {description}")
                print(f"{masked_acc_from} -> {masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            elif "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"{masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            else:
                print(f"{correct_date} {description}")
                print(f"{masked_card_from} -> {masked_card_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')

main()