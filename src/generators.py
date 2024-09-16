
def filter_by_currency(transactions, currency_code):
    """ принимает на вход список словарей, представляющих транзакции.
        возвращает операции соответствующие заданной валюте"""
    filtered_transactions = []
    for transaction in transactions:
        # Проверяем валюту транзакции
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            # Добавляем транзакцию в список,
            filtered_transactions.append(transaction)
    # Возвращаем список подходящих транзакций
    return filtered_transactions


def transaction_descriptions(transactions):
    """принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction.get("description", "Без описания")


def card_number_generator(start, stop):
    """ выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты"""
    # Проверяем, что начальное и конечное значения находятся в допустимом диапазоне
    if not (1 <= start <= 9999999999999999) or not (1 <= stop <= 9999999999999999):
        raise ValueError("Числа должны быть в диапазоне от 1 до 9999999999999999.")

    for number in range(start, stop + 1):
        # Форматируем номер карты в нужный формат
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
                                                                         8:12] + " " + f"{number:016d}"[12:]


