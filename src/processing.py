from typing import Any


def filter_by_state(data, state):
    """Функция фильтрует данные по указанному состоянию"""
    # print(data)
    # d = []
    # for i in data:
    #     if i.get("state") == state:
    #         d.append(i)
    #     else:
    #         continue
    # print(d)
    # return d
    return [d for d in data if d.get('state') == state]


# def sort_by_date(list_d: list[dict[str, Any]], reverse: str) -> Any:
#     """Сортировка списка словарей по дате в порядке убывания"""
#     sorted_list = []
#     for i in list_d:
#         if "date" in i:
#             if reverse == "в порядке убывания":
#                 sorted_list = sorted(list_d, key=lambda x: x.get['date'], reverse=True)
#             elif reverse == "в порядке возрастания":
#                 sorted_list = sorted(list_d, key=lambda x: x.get['date'])
#             else:
#                 sorted_list = sorted(list_d, key=lambda x: x.get['date'], reverse=True)
#         else:
#             return "Даты нет"
#     return sorted_list

def sort_by_date(date_list: Any, direction: bool = True) -> list:
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda x: x.get("date"), reverse=direction)
    return sorted_list

# data_1 = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# state = input().upper()
# if __name__ == "__main__":
#     print(filter_by_state(data_1, state))

