import pytest
from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    # Тестирование правильности маскирования номера карты
    assert get_mask_card_number("1234567890123456") == "123456** **** 3456"
    assert get_mask_card_number("9876543212345678") == "987654** **** 5678"

    # Проверка на пустую строку
    assert get_mask_card_number("") == "**** **** **** ****"

    # Проверка на строку, не являющуюся номером карты
    assert get_mask_card_number("ABCD123456") == "ABCD** **** "
    assert get_mask_card_number("123456A") == "123456** **** "


def test_get_mask_account():
    # Тестирование правильности маскирования номера счета
    assert get_mask_account("123456789012") == "**9012"
    assert get_mask_account("9876543210") == "**3210"

    # Проверка на пустую строку
    assert get_mask_account("") == "**"

    # Проверка на строку, не являющуюся номером счета
    assert get_mask_account("ACCOUNT1234") == "**1234"


if __name__ == "__main__":
    pytest.main()


@pytest.mark.parametrize("card_number, expected", [
    ("1234567890123456", "123456** **** 3456"),
    ("9876543212345678", "987654** **** 5678"),
    ("1234", "1234** ****"),
    ("", "**** **** **** ****")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

@pytest.mark.parametrize("account_number, expected", [
    ("123456789012", "**9012"),
    ("9876543210", "**3210"),
    ("12", "**12"),
    ("", "**"),
    ("ACCOUNT1234", "**1234"),
])
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected

