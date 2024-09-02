from typing import Union

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Обрабатывает информацию о картах и счетах и возвращает замаскированный номер."""
    parts = info.split()  # Разделяем строку на части
    account_type = " ".join(parts[:-1])  # Все части кроме последней - это тип
    account_number = parts[-1]  # Последняя часть - это номер

    if "Счет" in account_type:
        return get_mask_account(account_number)
    else:
        return get_mask_card_number(account_number)


# проверка
print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 7000792289606361"))
print(mask_account_card("Счет 73654108430135874305"))


def get_date(date_str: Union[str]) -> Union[str]:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    # Разбиваем строку по символу 'T' и берём первую часть (дату)
    date_part = date_str.split("T")[0]
    # Разбиваем дату на компоненты (год, месяц, день)
    year, month, day = date_part.split("-")
    # Формируем строку в нужном формате "ДД.ММ.ГГГГ"
    return f"{day}.{month}.{year}"


# проверка
print(mask_account_card("MasterCard 7158300734726758"))
print(get_date("2024-08-31T02:26:18.671407"))
