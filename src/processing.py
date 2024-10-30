def filter_by_state(data, state):
    """Функция фильтрует данные по указанному состоянию"""
    return [d for d in data if d.get('state') == state]


def sort_by_date(date_list, direction=True):
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda x: x.get("date"), reverse=direction)
    return sorted_list

# data_1 = [
#         {"id": 41428829, "state": "EXECUTED", "date": "2018-10-14T08:21:33.419441"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# user_state = input().upper()
# state = (f"'{user_state}'")
# if __name__ == "__main__":
#     print(filter_by_state(data_1, 'state'))
#     print(data_1)
#     print(state)
