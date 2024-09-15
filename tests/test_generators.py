import unittest

from parameterized import parameterized

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

class TestFilterByCurrency(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Фикстура для установки тестовых данных."""
        cls.transactions = [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]

    @parameterized.expand([
        ("USD", 3, [939719570, 142264268, 895315941]),
        ("RUB", 2, [873106923, 594226727]),
        ("GBP", 0, []),  # нет транзакций в GBP
        ("XYZ", 0, []),  # несуществующий код валюты
    ])
    def test_filter_by_currency(self, currency_code, expected_count, expected_ids):
        """Тестирование фильтрации транзакций по валюте."""
        result = filter_by_currency(self.transactions, currency_code)
        self.assertEqual(len(result), expected_count)
        self.assertEqual([transaction['id'] for transaction in result], expected_ids)


if __name__ == '__main__':
    unittest.main()


class TestTransactionDescriptions(unittest.TestCase):

    def test_descriptions_with_valid_transactions(self):
        """Тестирование функции с валидными транзакциями"""
        transactions = [
            {"description": "Перевод организации"},
            {"description": "Оплата товара"},
            {"description": "Снятие наличных"}
        ]
        descriptions = list(transaction_descriptions(transactions))
        expected_descriptions = ["Перевод организации", "Оплата товара", "Снятие наличных"]
        self.assertEqual(descriptions, expected_descriptions)

    def test_descriptions_with_empty_list(self):
        """Тестирование функции с пустым списком"""
        transactions = []
        descriptions = list(transaction_descriptions(transactions))
        expected_descriptions = []
        self.assertEqual(descriptions, expected_descriptions)

    def test_descriptions_with_missing_description(self):
        """Тестирование функции с транзакциями без описания"""
        transactions = [
            {"description": "Перевод организации"},
            {},  # Это транзакция без описания
            {"description": "Покупка"}
        ]
        descriptions = list(transaction_descriptions(transactions))
        expected_descriptions = ["Перевод организации", "Без описания", "Покупка"]
        self.assertEqual(descriptions, expected_descriptions)

    def test_descriptions_with_some_missing(self):
        """Тестируем с транзакциями, где некоторые описания отсутствуют."""
        transactions = [
            {"description": "Перевод на счет"},
            {"description": None},  # Это также считается отсутствующим описанием
            {}
        ]
        descriptions = list(transaction_descriptions(transactions))
        expected_descriptions = ["Перевод на счет", "Без описания", "Без описания"]
        self.assertEqual(descriptions, expected_descriptions)


if __name__ == '__main__':
    unittest.main()


class TestCardNumberGenerator(unittest.TestCase):
    @parameterized.expand([
        (1, 5, [
            "0000000000000001",
            "0000000000000002",
            "0000000000000003",
            "0000000000000004",
            "0000000000000005"
        ]),
        (100, 105, [
            "0000000000000100",
            "0000000000000101",
            "0000000000000102",
            "0000000000000103",
            "0000000000000104",
            "0000000000000105"
        ]),
        (10, 15, [
            "0000000000000010",
            "0000000000000011",
            "0000000000000012",
            "0000000000000013",
            "0000000000000014",
            "0000000000000015"
        ]),
        (9999999999999900, 9999999999999905, [
            "9999999999999900",
            "9999999999999901",
            "9999999999999902",
            "9999999999999903",
            "9999999999999904",
            "9999999999999905"
        ]),
    ])
    def test_card_number_generator(self, start, end, expected_numbers):
        """Тестируем генератор номеров карт с параметризацией."""
        result = list(card_number_generator(start, end))
        self.assertEqual(result, expected_numbers)

    def test_card_number_generator_empty(self):
        """Тестируем генератор с пустым диапазоном (start больше end)."""
        result = list(card_number_generator(5, 1))
        self.assertEqual(result, [])  # Ожидаем пустой список

if __name__ == '__main__':
    unittest.main()
