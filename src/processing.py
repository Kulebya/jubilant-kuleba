from typing import Dict, List


def filter_by_state(transactions: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по значению ключа 'state'."""
    filtered_transactions = [transaction for transaction in transactions if transaction.get("state") == state]
    return filtered_transactions


def sort_by_date(transactions: List[Dict], descending: bool = True) -> List[Dict]:
    """Сортирует список словарей по дате в указанном порядке."""
    return sorted(transactions, key=lambda x: x["date"], reverse=descending)