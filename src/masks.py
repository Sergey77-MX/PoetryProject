import logging
from pathlib import Path

PATH_TO_PROJECT = Path(__file__).resolve().parent.parent
PATH_TO_FILE = PATH_TO_PROJECT / "data" / "operations.json"

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(PATH_TO_PROJECT / "logs" / "masks.log", encoding="UTF-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_numb: str) -> str:
    """Функция маскировки номера банковской карты"""

    numb_out = ""
    if len(card_numb) == 16:
        if card_numb.isdigit():
            logger.info("Получаем реквизиты карты дял шифрования номера")
            numb_out = ' '.join(card_numb[i:i + 4] for i in range(0, len(card_numb), 4))
        else:
            logger.error("Ошибка! некорректный ввод реквизитов карты")
            return "номер введен не корректно"
    else:
        logger.error("Ошибка! некорректный ввод реквизитов карты")
        return "номер введен не корректно"
    return numb_out[0:7] + "** **** " + numb_out[-4:]


def get_mask_account(account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(account) == 20:
        if account.isdigit():
            logger.info("Получаем реквизиты счета дял шифрования номера")
            return "**" + account[-4:]
        else:
            logger.error("Ошибка! некорректный ввод реквизитов счета")
            return "номер введен не корректно"
    else:
        logger.error("Ошибка! некорректный ввод реквизитов счета")
        return "номер введен не корректно"
