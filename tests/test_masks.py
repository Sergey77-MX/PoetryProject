import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('numb, mask_numb', [
    ('1234567898765432', '1234 56** **** 5432'),
    ('123456789876543', 'номер введен не корректно'),
    ('12345678987654321', 'номер введен не корректно'),
    ('', 'номер введен не корректно')
])
def test_get_mask_card_number(numb: str, mask_numb: str) -> None:
    assert get_mask_card_number(numb) == mask_numb


@pytest.mark.parametrize('numb, mask_numb', [
    ('12345678987654321874', '**1874'),
    ('1234567898765432187', 'номер введен не корректно'),
    ('123456789876543218745', 'номер введен не корректно'),
    ('', 'номер введен не корректно')
    ])
def test_get_mask_account(numb: str, mask_numb: str) -> None:
    assert get_mask_account(numb) == mask_numb
