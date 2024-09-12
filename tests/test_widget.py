import pytest

from src.widget import mask_account_card, get_date
from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("input_str, expected_output", [
    ("Счет 123456789012", "**** **** **** 012"),
    ("Карта 1234567890123456", "123456** **** 3456"),
    ("Счет 987654321", "**** **** **** 321"),
    ("Карта 1111222233334444", "111122** **** 4444"),
])
def test_mask_account_card_valid(mock_mask_account, mock_mask_card_number, input_str, expected_output):
    result = mask_account_card(input_str)
    assert result == expected_output


# Тесты для mask_account_card на некорректный ввод
def test_mask_account_card_invalid_input():
    with pytest.raises(ValueError, match="Некорректный формат ввода. Ожидалась строка вида '<Тип> <номер>'."):
        mask_account_card("Некорректный ввод")  # Нет номера

    with pytest.raises(ValueError, match="Некорректный формат ввода. Ожидалась строка вида '<Тип> <номер>'."):
        mask_account_card("Карта")  # Нет номера


@pytest.mark.parametrize("date_str, expected_output", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2023-12-25T15:30:00", "25.12.2023"),
    ("2022-01-01T00:00:00", "01.01.2022"),
])
def test_get_date_valid(date_str, expected_output):
    result = get_date(date_str)
    assert result == expected_output


# Тесты для get_date на некорректный ввод
def test_get_date_invalid_format():
    with pytest.raises(ValueError, match="Некорректный формат даты. Ожидалась строка вида 'ГГГГ-ММ-ДДTЧЧ:ММ:СС'."):
        get_date("Некорректная дата")  # Общий некорректный формат

    with pytest.raises(ValueError, match="Некорректный формат даты. Ожидалась строка вида 'ГГГГ-ММ-ДДTЧЧ:ММ:СС'."):
        get_date("2024-03-11")  # Нет символа 'T'

    with pytest.raises(ValueError, match="Некорректный формат даты. Ожидалась строка вида 'ГГГГ-ММ-ДДTЧЧ:ММ:СС'."):
        get_date("")  # Пустая строка
