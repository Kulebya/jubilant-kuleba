from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """Форматирует номер, показывая первые 6 и последние 4 цифры, а другие заменяя на *"""
    masked_card_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return masked_card_number


print(get_mask_card_number("1234567898765432"))


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """Форматирует номер так, чтобы показать последние 4 цифры, а перед ними – две звездочки"""
    masked_account_number = f"**{account_number[-4:]}"
    return masked_account_number


print(get_mask_account("1234567898765432"))
