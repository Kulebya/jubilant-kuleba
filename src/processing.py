from typing import List, Dict, Optional


def filter_by_state(transactions: List[Dict], state: Optional[str] = 'EXECUTED') -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_transactions = [transaction for transaction in transactions if transaction.get('state') == state]
    return filtered_transactions


# Проверка
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

print(filter_by_state(transactions))
print(filter_by_state(transactions, 'CANCELED'))


def sort_by_date(transactions: List[Dict], descending: Optional[bool] = True) -> List[Dict]:
    """Сортирует список словарей по дате в указанном порядке."""
    return sorted(transactions, key=lambda x: x['date'], reverse=descending)


# Пример входных данных для проверки функции
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

# Вызов функции для сортировки по убыванию
sorted_transactions_descending = sort_by_date(transactions)
print(sorted_transactions_descending)  # Вывод: список транзакций отсортированный по дате (убывание)

# Вызов функции для сортировки по возрастанию
sorted_transactions_ascending = sort_by_date(transactions, descending=False)
print(sorted_transactions_ascending)  # Вывод: список транзакций отсортированный по дате (возрастание)
