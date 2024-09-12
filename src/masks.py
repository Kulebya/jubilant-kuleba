from typing import Union


def get_mask_card_number(card_number: str) -> str:
    """Форматирует номер, показывая первые 6 и последние 4 цифры, а остальные замещая на *"""
    if not card_number:  # Если строка пустая
        return "**** **** **** ****"  # Пустая строка

    if len(card_number) < 6:  # Если длина меньше 6, показываем цифры и заменяем на *
        return f"{card_number}** ****"

    if len(card_number) >= 16:  # Обработка стандартного случая
        return f"{card_number[:6]}** **** {card_number[-4:]}"

    return f"{card_number}** ****"  # Если длина номера меньше 16, просто маскируем часть


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Форматирует номер так, чтобы показать последние 4 цифры, а перед ними – две звездочки"""
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number
