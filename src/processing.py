from typing import List, Dict, Any


def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция фильтрует данные по указанному состоянию"""
    return [d for d in data if d.get('state') == state]


def sort_by_date(date_list: list, reverse_list: bool = True) -> list | bool:
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda date_dict: date_dict.get("date"), reverse=reverse_list)
    return sorted_list
