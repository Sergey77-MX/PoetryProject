from typing import List, Dict, Any


def filter_by_state(data: list[dict[str, Any]], state: str = 'EXECUTED') -> list[dict[str, Any]]:
    """Функция фильтрует данные по указанному состоянию"""
    return [d for d in data if d.get('state') == state]


def sort_by_date(date_list: list[dict[str, Any]], direction: bool = True) -> list[dict[str, Any]]:
    """Функция сортировки списка словарей по дате"""
    sorted_list = sorted(date_list, key=lambda x: x.get("date"), reverse=direction)
    return sorted_list
