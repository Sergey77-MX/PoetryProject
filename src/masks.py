def get_mask_card_number(card_numb: str) -> str:
    """Функция маскировки номера банковской карты"""

    numb_out = ""
    if len(card_numb) == 16:
        if card_numb.isdigit():
            numb_out = ' '.join(card_numb[i:i + 4] for i in range(0, len(card_numb), 4))
        else:
            return "номер введен не корректно"
    else:
        return "номер введен не корректно"
    return numb_out[0:7] + "** **** " + numb_out[-4:]


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счета"""
    return "**" + account[-4:]
