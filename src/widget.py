from typing import Union


def mask_account_card(card: Union[str]) -> Union[str]:
    """Принимает строку, содержащую тип и номер карты или счета.
    Возвращает строку с замаскированным номером"""
    if "Счет" in card:
        return f"{card[:5]}**{card[-4:]}"
    else:
        return f"{card[:-12]} {card[-12:-18]} ** **** {card[-4:]}"


def get_date(date_str: Union[str]) -> Union[str]:
    """принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    # Разбиваем строку по символу 'T' и берём первую часть (дату)
    date_part = date_str.split("T")[0]
    # Разбиваем дату на компоненты (год, месяц, день)
    year, month, day = date_part.split("-")
    # Формируем строку в нужном формате "ДД.ММ.ГГГГ"
    return f"{day}.{month}.{year}"


print(mask_account_card("MasterCard 7158300734726758"))
print(get_date("2024-08-31T02:26:18.671407"))
