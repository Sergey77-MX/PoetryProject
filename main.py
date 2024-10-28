import os

from _datetime import datetime

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.utils import PATH_TO_FILE, financial_transactions
from src.reader_data_csv import reader_file_transaction_csv, PATH_TO_CSV
from src.reader_data_excel import reader_file_transaction_excel, PATH_TO_EXCEL


def main():
    """Отвечает за основную логику проекта с пользователем и связывает функциональности между собой."""
    global list_by_status, filter_transaction_date

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
    print(transactions_from_file)
    # return
    list_by_status = []
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
        # state = (f"'{user_state}'")
        list_by_status = filter_by_state(transactions_from_file, user_state)
        # list_by_state.append(list_by_status)
        print(f"Операции отфильтрованы по статусу {user_state}")
        # print(transactions_from_file)
        print(user_state)
        print(list_by_status)

    print("Отсортировать операции по дате? Да/Нет")

    filter_transaction_date = []
    user_input_date = input().lower()
    if user_input_date == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        user_input = input().lower()
        if user_input == "по убыванию":
            filter_transaction_date = sort_by_date(list_by_status)
            # user_input_up_down == True
        elif user_input == "по возрастанию":
            direction = False
            # user_input_up_down == False
            filter_transaction_date = sort_by_date(list_by_status, direction)
        else:
            print("Введен некорректный ответ.")
            # return
    elif user_input_date == "нет":
        filter_transaction_date = list_by_status
    else:
        print("Введен некорректный ответ.")
    print(filter_transaction_date)
        # return

    rub_trans = []
    print("Выводить только рублевые транзакции? Да/Нет")
    user_input_curr = input().lower()
    if user_input_curr == "да":
        for trans in filter_transaction_date:
            if trans["operationAmount"]["currency"]["code"] == "RUB":
                rub_trans.append(trans)
    elif user_input_curr == "нет":
        rub_trans = filter_transaction_date
        # for trans in filter_transaction_date:
        #     rub_trans.append(trans)
    else:
        print("Введен некорректный ответ.")
        # return

    # rub_trans = []
    trans_word = []
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    sort_by_word = input("Введите да или нет: ").lower()
    if sort_by_word == "да":
        sort_by_word_yes = input("Введите слово для фильтрации: ")
        trans_word = []
        for trans in rub_trans:
            if sort_by_word_yes in trans["description"]:
                trans_word.append(trans)
    elif sort_by_word == "нет":
        trans_word = []
        for trans in rub_trans:
            trans_word.append(trans)
    else:
        print("Введен некорректный ответ.")
        # return
    if len(trans_word) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        # return

    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(trans_word)}\n")

    for trans in trans_word:
        if trans.get("from") and trans.get("to"):
            date = trans.get("date", "")[:19]
            bad_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
            correct_date = bad_date.strftime("%d.%m.%Y")
            description = trans.get("description", "")
            masked_card_from = get_mask_card_number(str(trans.get("from")))
            masked_card_to = get_mask_card_number(str(trans.get("to")))
            masked_acc_from = get_mask_account(str(trans.get("from")))
            masked_acc_to = get_mask_account(str(trans.get("to")))
            amount = trans["operationAmount"]["amount"]
            if "Счет" in trans.get("from", "") and "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_acc_from} -> Счет: {masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            elif "Счет" in trans.get("to", ""):
                print(f"{correct_date} {description}")
                print(f"Счет: {masked_acc_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')
            else:
                print(f"{correct_date} {description}")
                print(f"Транзакция: {masked_card_from} -> {masked_card_to}")
                if trans.get("code") == "RUB":
                    print(f"Сумма: {amount} руб.\n")
                else:
                    print(f'Сумма: {amount} {trans["operationAmount"]["currency"]["code"]}\n')


main()


# from src.utils import financial_transactions, PATH_TO_FILE
# from src.reader_data_csv import reader_file_transaction_csv, PATH_TO_CSV
# from src.reader_data_excel import reader_file_transaction_excel, PATH_TO_EXCEL
# from src.processing import filter_by_state
#
# path = PATH_TO_FILE
# path_csv = PATH_TO_CSV
# path_xlsx = PATH_TO_EXCEL
#
#
#
#
# list_by_state = []
# # res = []
#
# # Функция приветствия.
# def main():
#     operations = []
#
#     print(f'''Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
#     1. Получить информацию о транзакциях из JSON-файла
#     2. Получить информацию о транзакциях из CSV-файла
#     3. Получить информацию о транзакциях из XLSX-файла''')
#
# # Получение информации о транзакциях
#     response = input()
#     if response == '1':
#         print('Для обработки выбран JSON-файл.')
#         operations = financial_transactions(path)
#
#     elif response == '2':
#         print('Для обработки выбран CSV-файл.')
#         operations = reader_file_transaction_csv(path_csv)
#
#     elif response == '3':
#         print('Для обработки выбран EXCEL-файл.')
#         operations = reader_file_transaction_excel(path_xlsx)
#
#
#     print(operations)
#
#
#
    # print('Введите статус, по которому необходимо выполнить фильтрацию. '
    #       'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
    # state = input("")
    # states_list = ['EXECUTED', 'CANCELED', 'PENDING']
    # while state.upper() not in states_list:
    #     print(f"Статус операции {state} недоступен.")
    #     print("Введите статус, по которому необходимо выполнить фильтрацию. "
    #           "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
    #     state = input()
    # else:
#         # Сортировка по статусу
#
#         print(filter_by_state(operations, "state"))
#         # print(operations)
#         # print(state)
#         print(f"Операции отфильтрованы по статусу {state}")
#         # print(list_by_state)
#
#         # return filter_by_state
#
# def sorting_by_status(operations_list, states):
#     list_by_status = filter_by_state(operations_list, 'states')
#     return list_by_status
#
# if __name__ == "__main__":
#     res = main()
# #      print(())
#
#
# # print(operations_list)
#
#



