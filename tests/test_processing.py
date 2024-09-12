import pytest
from src.processing import filter_by_state, sort_by_date

mock_transactions = [
    {"id": 1, "date": "2024-03-11", "state": "EXECUTED"},
    {"id": 2, "date": "2024-03-10", "state": "PENDING"},
    {"id": 3, "date": "2024-03-09", "state": "EXECUTED"},
    {"id": 4, "date": "2024-03-08", "state": "CANCELLED"},
]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 1, "date": "2024-03-11", "state": "EXECUTED"},
        {"id": 3, "date": "2024-03-09", "state": "EXECUTED"},
    ]),
    ("PENDING", [
        {"id": 2, "date": "2024-03-10", "state": "PENDING"},
    ]),
    ("CANCELLED", [
        {"id": 4, "date": "2024-03-08", "state": "CANCELLED"},
    ]),
    ("NON_EXISTENT", []),  # Для проверка случая, когда состояния нет
])
def test_filter_by_state(state, expected):
    result = filter_by_state(mock_transactions, state)
    assert result == expected


# Тестирование функции sort_by_date
def test_sort_by_date():
    sorted_transactions = sort_by_date(mock_transactions)
    assert sorted_transactions[0]["date"] == "2024-03-11"  # Должен быть самый недавний
    assert sorted_transactions[1]["date"] == "2024-03-10"
    assert sorted_transactions[2]["date"] == "2024-03-09"
    assert sorted_transactions[3]["date"] == "2024-03-08"


# Тестирование сортировки по убыванию
def test_sort_by_date_descending():
    sorted_transactions = sort_by_date(mock_transactions, descending=False)
    assert sorted_transactions[0]["date"] == "2024-03-08"  # Должен быть самый ранний
    assert sorted_transactions[1]["date"] == "2024-03-09"
    assert sorted_transactions[2]["date"] == "2024-03-10"
    assert sorted_transactions[3]["date"] == "2024-03-11"


# Тесты на некорректные входные данные
def test_filter_by_state_invalid():
    with pytest.raises(TypeError):
        filter_by_state("not a list", "EXECUTED")

    with pytest.raises(TypeError):
        filter_by_state(mock_transactions, 123)  # состояние должно быть строкой


def test_sort_by_date_invalid():
    with pytest.raises(TypeError):
        sort_by_date("not a list", True)

    with pytest.raises(KeyError):
        sort_by_date([{"date": "2024-03-11"}, {"state": "EXECUTED"}])  # Отсутствует ключ 'date'