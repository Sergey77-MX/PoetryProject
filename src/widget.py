import masks

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
        numb_mask = masks.get_mask_card_number(numb)
        mask = name + numb_mask
        return mask
    else:
        numb_mask = masks.get_mask_account(numb)
        mask = name + numb_mask
        return mask



def get_date():

    pass
