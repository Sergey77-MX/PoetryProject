from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция для обработки информации о картах и счетах.
    Возвращает замаскированный номер"""
    numb = ""
    name = ""
    for c in card:
        if c.isdigit():
            numb += str(c)
        else:
            name += str(c)
    if len(numb) == 16:
        numb_mask = get_mask_card_number(numb)
        mask = name + numb_mask
        return mask
    else:
        numb_mask = get_mask_account(numb)
        mask = name + numb_mask
        return mask


def get_date(raw_date: str) -> str:
    """Функция принимает на вход строку с датой в формате '2024-03-11T02:26:18.671407'
 и возвращает строку с датой в формате 'ДД.ММ.ГГГГ'"""
    slice_date = raw_date[:10]
    date_clear = ""
    for one_symbol in range(len(slice_date)):
        if slice_date[one_symbol].isdigit():
            date_clear += slice_date[one_symbol]
        else:
            date_clear += " "
    date_clear_split = date_clear.split()
    split_date = date_clear_split[::-1]
    final_result = ".".join(split_date)
    return final_result
