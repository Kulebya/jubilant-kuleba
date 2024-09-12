import pytest

@pytest.fixture
def card_numbers():
    return [
        ("1234567890123456", "123456** **** 3456"),
        ("9876543212345678", "987654** **** 5678"),
        ("1234", "1234** ****"),
        ("", "**** **** **** ****"),
        ("123456A", "123456** ****"),
    ]

@pytest.fixture
def account_numbers():
    return [
        ("123456789012", "**9012"),
        ("9876543210", "**3210"),
        ("12", "**12"),
        ("", "**"),
        ("ACCOUNT1234", "**1234"),
    ]

# Фикстуры для моков
@pytest.fixture
def mock_mask_account(mocker):
    return mocker.patch("masks.get_mask_account", return_value="**** **** **** 012")

@pytest.fixture
def mock_mask_card_number(mocker):
    return mocker.patch("masks.get_mask_card_number", return_value="123456** **** 3456")