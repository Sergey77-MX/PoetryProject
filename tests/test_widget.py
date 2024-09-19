import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('card, mask_card', [
    ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
    ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
    ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
    ('Счет 73654108430135874305', 'Счет **4305')
])
def test_mask_account_card(card: str, mask_card: str) -> None:
    assert mask_account_card(card) == mask_card


def test_get_date(date: str) -> None:
    assert get_date('2024-03-11T02:26:18.671407') == date
